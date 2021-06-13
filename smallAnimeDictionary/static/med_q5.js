// if this is the last question, then nextQ = null
let quizType = 'Intermediate'
let qNum = 5
let question = 'What <span class="boldTxt">term</span> best conveys what type of character is in<span class="boldTxt"> media below?</span>'
let hint = 'baka roughly translates to idiot in Japanese'
let answer = 'tsundere'
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
