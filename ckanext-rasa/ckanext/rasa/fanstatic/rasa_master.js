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
  if (text){
    _append(text, true)

    chatbox.animate({scrollTop: chat_start.height() }, "slow")

    $(document).ajaxStart(function(){
    }).ajaxStop(function(){
    })

    $("#user-input").val('')
    // Make AJAX request. Check that not wewaiting for AJAX request, otherwise void input
    response = send_user_message(url, "POST", text).then(
      bot_response,
      handle_request_error
    )
  }
}

function _append(text, is_human){
  message = format_incoming_message(text, is_human)
  li = construct_li(message)
  $("#chat-start").append(li)
}

// Bot responses

function handle_request_error(response){
  _append("ERROR 404: something went seriously wrong", false)
}


function bot_response(response){
  console.log(response)
  if (response["error"]){
    // Handle error
    return
  }
  // Bot's response is a list
  for (i in response["bot"]) {
    _append(response["bot"][i], false)
  }
  // _append(response["bot"], false)
}

// AJAX using promises

function send_user_message(url, methodType, text){
  data = {
    "text" : text
  }
  return $.ajax({
    url: url,
    method: methodType,
    data: JSON.stringify(data),
    contentType: "application/json",
    dataType: "json"
  })
}


// Format incoming messages

function format_incoming_message(text, is_human){
  /*Create message object*/

  // Converts \n given in python to breakline suitable for HTML
  console.log(text)
  text = text.replace(/\n/g, "<br>")
  time = _get_time()
  return {
    payload: text,
    time: time,
    human: ((is_human) ? "human" : "bot")
  }
}

function _get_time(){
  /*Returns current time in HR:MM {AM,PM} */
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

function construct_li(message){
  /*Construct li to be appended*/
  a = '<li class="message" id="'
  b = '">'
  c = "</li>"
  message = a + message.human + b + message.time + ": " + message.payload + c
  return message
}
