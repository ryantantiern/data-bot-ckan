var chatbox = $(".chatbox")
$("#user-input").val('')
chatbox.scrollTop = chatbox.scrollHeight - chatbox.clientHeight

function submit_query(form){
  /*Entry from DOM*/
  if (form.elements["user-input"].value){
    // Make AJAX request. Check that not wewaiting for AJAX request, otherwise void input
    _append(form.elements["user-input"].value, true)
    $("#user-input").val('')
  }
}


function _append(text, is_human){
  message = format_incoming_message(text, is_human)
  li = construct_li(message)
  console.log(li)
  $("#chat-start").append(li)
}

// Format incoming messages

function format_incoming_message(text, is_human){
  /*Create message object*/
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
