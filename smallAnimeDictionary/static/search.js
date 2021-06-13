let displayMatch = function (anime_term_from_DB) {
  let newMatch =$('<div class="col-12 text-center"></div>') 
  let newLink = $('<button class="btn btn-link resultFormat" type="button">'+anime_term_from_DB.title+'</button>')
  $(newLink).click(function () {
    window.location.href='/view/'+ anime_term_from_DB.id 
  })
  newMatch.append(newLink)
  $('#results_container').append(newMatch)
  //$('#results_container').append(newLink)

}

let displayNoResultsInfo = function () {
  let noResultsText = $('<div class="col-12 text-center resultFormat mb-1">No Results</div>')
  let noResultsImg = $('<div class="col-12 text-center"></div>')
  let noResultsImgSrc = $('<img src="https://pa1.narvii.com/5887/e89e2d9c4118be30a2f7831eaf43658b910c830f_00.gif" alt="anime image">')
  noResultsImg.append(noResultsImgSrc)
  $('#results_container').append(noResultsText)
  $('#results_container').append(noResultsImg)

}


let displaySearchResults = function() {
  $('#results_container').empty()
  //$('#numResultsContainer').empty()
  let count = 0

  $.each(anime_db, function(i, anime_term_from_DB){
    let isTitleInDB = anime_term_from_DB.title.toLowerCase().includes(searchQuery.toLowerCase())

    if (isTitleInDB) {
      // create array with spaces
      displayMatch(anime_term_from_DB) 

      count = count + 1
    } 

 }) // end of each

 //detail number of results
 let numResult = $('<h2 class="mb-1">'+count+' Results:</h2>')
 $('#resultsNumContainer').append(numResult)

 console.log(count)
 if (count < 1) {
   displayNoResultsInfo()
 }
}



$(document).ready(function(){
    displaySearchResults()
})






