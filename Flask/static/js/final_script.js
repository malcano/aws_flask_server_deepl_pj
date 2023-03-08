// document.querySelectorAll(".gallery").forEach(function(gal) {
//     var imgsCont = gal.querySelector(".images-container"),
//         imgs = imgsCont.querySelectorAll(".images"),
//         product = gal.closest(".shop").querySelector(".product"),
//         controls = gal.querySelector(".controls");
    
//     if (imgsCont.querySelectorAll(".images.active").length == 0){
//       imgsCont.querySelector(".images").classList.add("active");
//     }
    
//     var imgsActive = imgsCont.querySelector(".images.active"),
//         activeOffset = imgsActive.offsetTop - imgsCont.offsetTop;
    
//     imgs.forEach(function(img) {
//       var childrenWidth = 0;
      
//       img.querySelectorAll("img").forEach(function(child) {
//         childrenWidth += child.offsetWidth;
//       });
      
//       img.style.width = childrenWidth + "px";
//     });
    
//     imgsCont.style.transform = "translate(0, -" + activeOffset + "px)";
    
//     product.querySelector(".options li:nth-child(" + (imgsActive.dataset.index) + ")").classList.add("active");
    
//     product.querySelectorAll(".options li").forEach(function(opt) {
//       opt.addEventListener("click", function(e) {
//         e.preventDefault();
        
//         var optIndex = this.dataset.index;
        
//         this.parentNode.querySelectorAll(".active").forEach(function(active) {
//           active.classList.remove("active");
//         });
//         this.classList.add("active");
        
//         var nextImgs = imgsCont.querySelector(".images[data-index='" + optIndex + "']"),
//             nextImgsoffset = nextImgs.offsetTop - imgsCont.offsetTop;
        
//         imgsCont.querySelector(".images.active").classList.remove("active");
//         nextImgs.classList.add("active");
        
//         imgsCont.style.transform = "translate(0, -" + nextImgsoffset + "px)";
//       });
//     });
    
//     imgs.forEach(function(img) {
//       if (img.querySelector(".active") == null) {
//         img.querySelector("img").classList.add("active");
//       }
//     });
    
//     function imgsNextImg() {
//       var activeImgs = imgsCont.querySelector(".images.active"),
//           acImg = activeImgs.querySelector("img.active"),
//           imgsImg = activeImgs.querySelectorAll("img"),
//           imgLen = imgsImg.length,
//           nextImgEq = 0;
      
//       if (acImg.dataset.index + 1 > imgLen - 1) {
//         nextImgEq = 0;
//       } else {
//         nextImgEq = parseInt(acImg.dataset.index) + 1;
//       }
      
//       var nextEq = activeImgs.querySelector("img[data-index='" + nextImgEq + "']"),
//           nextOffset = nextEq.offsetLeft - activeImgs.offsetLeft;
      
//       acImg.classList.remove("active");
//       nextEq.classList.add("active");
      
//       activeImgs.style.transform = "translate(-" + nextOffset + "px, 0)";
//     }
//   });
  
	
// 	function imgsPrevImg(){
		
// 		var activeImgs = imgsCont.find(".images.active"),
// 				acImg = activeImgs.find("img.active"),
// 				imgsImg = activeImgs.find("img"),
// 				imgLen = imgsImg.length,
// 				nextImgEq = 0
		
// 		if (acImg.index() - 1 < 0){
// 			nextImgEq = imgLen - 1
// 		}else{
// 			nextImgEq = acImg.index() - 1
// 		}
		
// 		var nextEq = activeImgs.find("img").eq(nextImgEq),
// 				nextOffset = nextEq.offset().left - activeImgs.offset().left
		
		
// 		acImg.removeClass("active");
// 		nextEq.addClass("active");
		
// 		activeImgs.css({"transform": "translate(-" + nextOffset + "px, 0)"})
		
// 	}
	
// 	$(controls).find(".arrows").find(".right").on('click', function(e){
// 		e.preventDefault();
// 		imgsNextImg()
// 	});
// 	$(controls).find(".arrows").find(".left").on('click', function(e){
// 		e.preventDefault();
// 		imgsPrevImg();
// 	});
	
