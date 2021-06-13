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

$(document).ready(function(){
  $('#search_entry').focus()
})