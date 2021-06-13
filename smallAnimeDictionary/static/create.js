let createSuccessHeader = function (newAnime) {
  let successHeader = $('<div id="jumbotron" class="py-5 pl-3 bg-success"> <h1>New item successfully created</h1> </div>)')

  let newDiv = $('<div>')
  let newLink = $('<button id="seeCreationBtn" class="btn btn-link" type="button">See it here</button>')
  newDiv.append(newLink)
  $(newLink).click(function(){
    window.location.href='/view/'+ newAnime.id
  })

  console.log("newAnime"+newAnime.genres)
  console.log(newAnime.genres)

$('#headerSuccessContainer').append(successHeader)
$('#headerSuccessContainer').append(newDiv)

}

let saveEntry = function(newEntry){
	$.ajax({
			type: "POST",
			url: "save_entry",                
			dataType : "json",
			contentType: "application/json; charset=utf-8",
			data : JSON.stringify(newEntry),
			success: function(data, text){
        let newAnimeEntry = data['new_anime_data']
        createSuccessHeader(newAnimeEntry)


		},
			error: function(request, status, error){
					console.log("Error");
					console.log(request)
					console.log(status)
					console.log(error)
			}
	})
}

let submitEntry = function () {
  // clear successHeader

  // grab
  let title = $.trim($('#writeTitle').val())
  let img  = $.trim($('#writeImg').val())
  let summary= $.trim($('#writeSummary').val())
  let score = $.trim($('#writeScore').val())
  let genres = $.trim($('#writeGenres').val())


  // empty container and errors
  $('#headerSuccessContainer').empty()
  $('#titleError').empty()
  $('#imgError').empty()
  $('#summaryError').empty()
  $('#scoreError').empty()
  $('#genresError').empty()
  // this has msg to see if creation was a success
  $('#LinkSuccessContainer').empty()

  //error detection

  if (genres == ''){
      let noGenres = $('<div class="badInput"> Enter Genres</div>')
      $('#genresError').append(noGenres)
      $('#writeGenres').focus()
  }
  let genreList = genres.split(',')
  console.log("after split:"+genreList)

  let isScoreNum = $.isNumeric(score)
  console.log("score:"+isScoreNum)
  if (score =='') {
    let noScore = $('<div>Enter a Score</div>')
    $('#scoreError').append(noScore)
    $('#writeScore').focus()
  } else if (isScoreNum == false) {
    let noScore = $('<div>Score is not a number</div>')
    $('#scoreError').append(noScore)
    $('#writeScore').val('')
    $('#writeScore').focus() 
  }

  if (summary ==''){
      let noSummary = $('<div class="badInput"> Please Provide a Summary </div>')
      $('#summaryError').append(noSummary)
      $('#writeSummary').focus()
  }

  let isImgJpg = img.endsWith(".jpg")
  console.log("img:"+isImgJpg)
  if (img ==''){
      let noImg = $('<div class="badInput"> Enter an Image </div>')
      $('#imgError').append(noImg)
      $('#writeImg').focus()
  } else if (isImgJpg == false) {
      let noImg = $('<div class="badInput"> Image must end in .jpg </div>')
      $('#imgError').append(noImg)
      $('#writeImg').val('')
      $('#writeImg').focus()
  }


  if (title =='') {
      let noTitle = $('<div class="badInput"> Enter a Title </div>')
      $('#titleError').append(noTitle)
      $('#writeTitle').focus()
  }


    if (title =='' || img =='' || isImgJpg == false || summary =='' || score =='' || isScoreNum == false || genres =='') {
      return false // prevents button from submitting
    } 

    // passed error checking so can create entry and clear data


    console.log("img"+img)

    let newEntry = {
      'title': title,
      'image': img, 
      'summary': summary,
      'score': score,
      'genres': genreList
    }

    console.log("newEntry img:"+newEntry.image)

    saveEntry(newEntry)

    // saveEntry(newEntry)
    // displayLink(newEntry)

  // reset all the values
   $('#writeTitle').val('')
   $('#writeImg').val('')
   $('#writeSummary').val('')
   $('#writeScore').val('')
   $('#writeGenres').val('')

  //return fcocus to title
  $('#writeTitle').focus()

}

$(document).ready(function(){
  $('#submit_btn').click(function () {
    submitEntry() 
  })
})

$(document).ready(function(){
  $('#writeTitle').focus()
})


