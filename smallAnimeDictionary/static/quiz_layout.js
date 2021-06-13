
// start of quiz part of layout

let setup_quiz_title = function (quizType) {
  $('#quizTitleContainer').empty()
  let quizTitleHtml = $('<span class="quizHeading">'+quizType+' Quiz</span>')
  $('#quizTitleContainer').append(quizTitleHtml)
}

let setup_question_position = function (qNum) {
  $('#questionPositionContainer').empty()
  let qNumHtml = $('<span class="text-muted">Question '+qNum+' of 5</span>')
  $('#questionPositionContainer').append(qNumHtml)
}

let setup_question = function (question) {
  $('#quizQuestionContainer').empty()
  console.log("inside setup: "+question)
  // you can't do '<span class="lead">'+question+'</span> for some reason
  let qHtml = $('<span class="lead">'+question+'</span>')
  $('#quizQuestionContainer').append(qHtml)
}

// i edited form-inline in layout to be margin auto to center input and btn
let setup_submit_quiz_btn = function () {
  $('#submitQuizBtnContainer').empty()
  let submitQuizHtml = $('<div class="form-inline d-inline-block"></div>')
  let inputHtml = $('<input type="text" class="d-inline-block form-control mr-2" id="writeTerm" placeholder="Type in Term"> required')
  let submitBtnHtml = $('<button class="btn btn-outline-info text-center" type="button">Submit</button>')
  submitQuizHtml.append(inputHtml)
  submitQuizHtml.append(submitBtnHtml)

  $(submitBtnHtml).click(function () {
    submit_user_answer(answer)
  })

  $('#submitQuizBtnContainer').append(submitQuizHtml)

}

// Submit Answer part of Quiz

let submit_user_answer = function (answer) {
  //grab user input
  let userInput = $.trim($('#writeTerm').val())

  $('#submitError').empty()

  if (userInput ==''){
    let noUserInput = $('<div> Enter a Term </div>')
    $('#submitError').append(noUserInput)
    // prevent button from submitting
    return false
  }

  //passed error checking for empty input can check answer

  // empty out submission and hint
  $('#submitQuizBtnContainer').empty()
  $('#hintContainer').empty()
  $('#hintMsgContainer').empty()


  //show userInput to user
  let userSeeInputHtml = $('<div class="text-center"><span class="text-muted">You entered </span> <span class="bigTxt">'+userInput+'<\span></div>')
  $('#userSeeInputContainer').append(userSeeInputHtml)

  // check if correct answer
  let userInputLowerCase = userInput.toLowerCase()
  console.log(userInputLowerCase)
  if(userInputLowerCase == answer){
    userCorrect()
    //increaseScore()
  }
  else {
    userIncorrect(answer)
  }

  // if last question - button should be see results
  // if not the last question button should be next question
  if(isLastQ){
    setup_seeResults_btn()
  }
  else {
    setup_next_btn(nextQ)
  }

}

let userCorrect = function () {
  let correctHtml = $('<div class="text-center"><span class="correctFormat bigTxt">Correct</span></div>')
  $('#correctContainer').append(correctHtml)

  // updates score in server
  increaseScore() 

}

let userIncorrect = function (answer) {


  let answerID = getTermID(answer)
  console.log(answerID)
  let answerLinkHtml = '<a href="/view/'+answerID+'">'+answer+'</a>'
  let incorrectHtml = $('<div class="text-center"><span class="incorrectFormat bigTxt">Incorrect</span> - <span class="text-muted">Correct answer is </span><span class="bigTxt">'+answerLinkHtml+'</span></div>')
  $('#incorrectContainer').append(incorrectHtml)
}

// get id of answer
let getTermID = function (answer) {
  for (let i = 0; i < anime_db.length; i++) {
    if(anime_db[i].title == answer)
      return anime_db[i].id
  }
}


// end of Submit part of quiz

let setup_hint_btn = function () {
  let hintBtnHtml = $('<button class="btn btn-primary" type="button">Need a Hint?</button>')
  $(hintBtnHtml).click(function () {
    setup_hint(hint)
  })

  $('#hintContainer').append(hintBtnHtml)
}

let setup_hint = function (hint) {
  $('#hintMsgContainer').empty()
  console.log("inside hint setup: "+hint)
  // you can't do '<span class="lead">'+question+'</span> for some reason
  let hintHtml = $('<span class="lead font-weight-bold">'+hint+'</span>')
  $('#hintMsgContainer').append(hintHtml)
}

let setup_next_btn = function(nextQ) {
  $('#nextQuestionContainer').empty()
  let nextBtnHtml = $('<button class="btn btn-warning" type="button">Next Question</button>')
  $(nextBtnHtml).click(function () {
    $('#quizQuestionContainer').empty()
    window.location.href = '/'+ nextQ
  })
  $('#nextQuestionContainer').append(nextBtnHtml)
}

let setup_seeResults_btn = function() {
  $('#seeResultsContainer').empty()
  let seeResultsBtnHtml = $('<button class="btn btn-outline-success btn-lg" type="button">See Quiz Results</button>')
  $(seeResultsBtnHtml).click(function () {
    window.location.href = '/quiz_results' 
  })
  $('#seeResultsContainer').append(seeResultsBtnHtml)
}

let increaseScore = function(){
	$.ajax({
			type: "POST",
			url: "/increase_score",                
			success: function(data){
		},
			error: function(request, status, error){
					console.log("Error");
					console.log(request)
					console.log(status)
					console.log(error)
			}
	})
}

let resetScore = function(){
	$.ajax({
			type: "POST",
			url: "/reset_score",                
			success: function(data){
		},
			error: function(request, status, error){
					console.log("Error");
					console.log(request)
					console.log(status)
					console.log(error)
			}
	})
}


// end of quiz part of layout

// animeterms

let formatTerms = function (animeTerm, count) {
  let newTerm = $('<div class="col-3 text-center mb-3">')
  let newLink = $('<button id="seeCreationBtn" class="termBtn btn btn-link" type="button">'+animeTerm.title+'</button>')
  // if count is > 3, means row is even. if < 3 row is odd
  if (count > 3) {
    newLink.addClass("term_bg1")
  }
  else {
    newLink.addClass("term_bg2")
  }
  $(newLink).click(function () {
    window.location.href='/view/'+ animeTerm.id 
  })
  newTerm.append(newLink)
  $('#terms_container').append(newTerm)
}



let displayTerms = function () {
  // count to keep track of rows. >3 means row is even, <3 row is odd
  let count = 0
  for (let i = 0; i < anime_db.length; i++){
    if (count == 8) {
      count = 0;
    }
    let animeTerm = anime_db[i]
    formatTerms(animeTerm, count)
    count++
  }

}

$(document).ready(function(){
  displayTerms()
})

// all the functions below are for the search bar on top
let search_entry = function () {
  let title = $('#search_entry').val()
  if (title ==''){
    return false
  }
  window.location.href='/search/'+ title 
}

$(document).ready(function(){
  $("#searchBtn").click(function(){                
    search_entry()
  })
})

$(document).ready(function(){
  $("#search_entry").keyup(function(e) {
    if (e.keyCode === 13) {
      search_entry()
    }
  })
})