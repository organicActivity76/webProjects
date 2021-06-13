// if this is the last question, then nextQ = null
let quizType = 'Advanced'
let qNum = 5
let question = 'What <span class="boldTxt">term</span> best represents the <span class="boldTxt">description below?</span>'
let hint = 'starts with an \'m\''
let answer = 'moe'
let nextQ = null 
let isLastQ = true 

$(document).ready(function(){
  setup_quiz_title(quizType)
  setup_question_position(qNum)
  setup_question(question)
  setup_submit_quiz_btn()
  setup_hint_btn()
})

$(document).ready(function(){
  $('#writeTerm').focus()
})

$(document).ready(function(){
  $("#writeTerm").keyup(function(e) {
    if (e.keyCode === 13) {
      submit_user_answer(answer)
    }
  })
})