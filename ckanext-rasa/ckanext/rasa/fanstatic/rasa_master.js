var chatbox = $(".chatbox")
var chat_start = $("#chat-start")
$("#user-input").val('')
chatbox.animate({scrollTop: chat_start.height() }, "slow")
BASE_URL = document.location.href

function submit_query(form){
  /*Entry from DOM*/
  route = "/user/message"
  url = BASE_URL + route
  text = form.elements["user-input"].value

  if (!is_malicious_text(text)) {
    
    _append(text, true)

    chatbox.animate({scrollTop: chat_start.height() }, "slow")

    $(document).ajaxStart(function () {
      // Loader goes in here

    }).ajaxStop(function () {

    })

    $("#user-input").val('')
    // Make AJAX request. Check that not we are not waiting for AJAX request, otherwise void input
    response = send_user_message(url, "POST", text).then(
      bot_response,
      handle_request_error
    )
  }
}
function is_malicious_text(text) {
  if (text.length < 2){
    _append("Message should be atleast 2 characters long. Plesae avoid using abbreviations.")
    return true
  }
  
  return false
}



// Bot responses

function handle_request_error(response) {
  console.log(response)
  _append("We're really sorry, DataBot couldn't process your message. This means the Rasa extension that hosts databot is down. Please report this to system administrators.", false)
}

function bot_response(response) {
  /**
   * Handles the returned data recursively. Data object
   * can either be of type "string", "list", or "*_object".
   * Each custom "*_object" type needs its own handler
   * 
   * response: Data object
   * 
   */
  response = response["bot"]
  console.log(response)
  if ($.isEmptyObject(response)) { 
    _append("No data received from CKAN server. Sorry about that!")
    return
  }
  handle_stack = [response]
  while (handle_stack.length > 0) {
    resp = handle_stack.pop()
    if (resp["type"] == "string") {
      _append(resp["data"], false)
    }
    else if (resp["type"] == "list") {
      for (i = resp["data"].length - 1; i > -1; i--) {
        resp["data"][i]["index"] = i
        handle_stack.push(resp["data"][i])
      }
    }
    else if (resp["type"] == "source_data_object") {
      message = format_source_data_object(resp)
      _append(message, false)
    }
    else {
      _append("CKAN controller returned a format that's undecipherable. Sorry about that!", false)
    }
  }
}

function format_source_data_object(data) {
  /**
   * Converts a SourceData object into a string
   * 
   * data: SourceData 
   */
  index = data["index"]
  organization = "Organization: " + data["org"]
  num_of_resources = "No. of resources: " + data["num_of_resources"]
  title = "Title: " + data["title"]
  message = index + ". " + title + "<br>" + organization + "<br>" + num_of_resources
  return message
}


function send_user_message(url, methodType, text) {
  /**
   * Sends an AJAX request to url with the method:methodType 
   * and payload:text. AJAX uses Promises. 
   * 
   * url: Str
   * methodType: Str
   * text: Str
   */
  data = {
    "text" : text
  }
  console.log("Sending message to: " + url)
  return $.ajax({
    url: url,
    method: methodType,
    data: JSON.stringify(data),
    contentType: "application/json",
    dataType: "json",
    timeout: 5000
  })
}


// Format incoming messages
function create_message_object(text, is_human){
  /**
   * Creates Message object
   * 
   * text: Str
   * is_human: bool
   */

  // Converts \n given in python to breakline suitable for HTML
  text = text.replace(/\n/g, "<br>")
  time = _get_time()
  return {
    payload: text,
    time: time,
    human: ((is_human) ? "human" : "bot"),
    
  }
}

function _get_time(){
  /**
   * Returns current time in HR:MM {AM,PM} 
   */

  date = new Date()
  time = [date.getHours(), ":", date.getMinutes(), " "]
  // Hour correction
  if (time[0] > 12) {
    time[0] = time[0] - 12
    time.push("PM")
  }
  else {
    if (time[0] == "0") time[0] = "12"
    time.push("AM")
  }
  // Minute correction
  if (time[2] < 10) time[2] = "0".concat(time[2])
  return time.join("")

}

function _append(text, is_human) {
  /**
   * Appends an li onto the ul tag with id chat-start. 
   * Text send to this method shouldn't require formatting anymore.
   * 
   * text: Str
   * is_human: bool
   */
  message = create_message_object(text, is_human)
  li = construct_li(message)
  $("#chat-start").append(li)
}

function construct_li(message){
  /**
   * Constructs a simple li with from the resulting message object. 
   * Sets the li to the appropriate id ("human"/"bot") for styling
   * 
   * message: Message
   */
  a = '<li class="message" id="'
  b = '">'
  c = "</li>"
  message = a + message.human + b + message.time + ": " + message.payload + "<br>" + c 
  return message
}
