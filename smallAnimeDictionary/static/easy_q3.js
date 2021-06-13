// if this is the last question, then nextQ = null
let quizType = 'Beginner'
let qNum = 3
let question = 'What <span class="boldTxt">term</span> best describes the <span class="boldTxt">pictures below? </span>' 
let hint = 'starts with a \'c\''
let answer = 'cosplay'
let nextQ = 'easy_q4' 
let isLastQ = false 

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

