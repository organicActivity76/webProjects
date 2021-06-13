// if this is the last question, then nextQ = null
let quizType = 'Beginner'
let qNum = 1
let question = 'What <span class="boldTxt">term</span> best represents the <span class="boldTxt">description below?</span>'
let hint = "this is a dictionary about... "
let answer = 'anime'
let nextQ = 'easy_q2'
let isLastQ = false

$(document).ready(function(){
  resetScore() // need for 1st question
  setup_quiz_title(quizType)
  setup_question_position(qNum)
  setup_question(question)
  setup_submit_quiz_btn()
  setup_hint_btn()
})

$(document).ready(function(){
  $('#writeTerm').focus()
})

// click enter to also submit answer
$(document).ready(function(){
  $("#writeTerm").keyup(function(e) {
    if (e.keyCode === 13) {
      submit_user_answer(answer)
    }
  })
})




