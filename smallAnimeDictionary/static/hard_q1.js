// if this is the last question, then nextQ = null
let quizType = 'Advanced'
let qNum = 1
let question = 'What <span class="boldTxt">term</span> best represents what <span class="boldTxt">genre</span> the <span class="boldTxt">pictures</span> belongs to?'
let hint = "stars with a \'y\' and ends in an \'i\'"
let answer = 'yaoi'
let nextQ = 'hard_q2'
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