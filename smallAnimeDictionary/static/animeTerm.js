let displayTermInfo = function () {
    let termDef = $('<div class="col-6"></div>')
    let termDefHeadingHtml = $('<div class = "col text-center defHeading mb-2">Definition</div>')
    let termDefinfo = $('<div class="col">'+animeTerm.def+'<div>')    
    termDef.append(termDefHeadingHtml)
    termDef.append(termDefinfo)
    //let termDef = $('<div class="col-6 align-self-center">'+animeTerm.def+'</div>')

    let termImg = $('<div class="col-6"></div>')
    let images = $('<div class="row"></div>')
    let imgTopRight = $('<div class="col mb-3 text-center"></div>')
    let img1 =  $('<img class="animeImgSize" src="'+animeTerm.img[0]+'"alt="anime image"</img>') 
    let imgBtmLeft =$('<div class="col text-center"></div>')
    let img2 = $('<img class="animeImgSize" src="'+animeTerm.img[1]+'"alt="anime image"</img>') 

    imgTopRight.append(img1)
    imgBtmLeft.append(img2)

    images.append(imgTopRight)
    images.append(imgBtmLeft)

    termImg.append(images)

    // console.log(animeTerm.img)
    console.log(animeTerm.img[0])

    $('#termInfo_container').append(termDef)
    $('#termInfo_container').append(termImg)
   
 
}
  
$(document).ready(function(){
     displayTermInfo()
})