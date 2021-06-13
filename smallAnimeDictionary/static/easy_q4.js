// if this is the last question, then nextQ = null
let quizType = 'Beginner'
let qNum = 4
let question = 'What <span class="boldTxt">term</span> best represents what <span class="boldTxt">genre/demographic</span> the <span class="boldTxt">description below</span> belongs to?'
let hint = 'starts with \'sh\''
let answer = 'shonen'
let nextQ = 'easy_q5' 
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

