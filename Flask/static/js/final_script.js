$(".gallery").each( function(){
	var gal = $(this),
			imgsCont = gal.find(".images-container"),
			imgs = imgsCont.find(".images"),
			product = gal.parents(".shop").find(".product"),
			controls = gal.find(".controls");
	
	if (imgsCont.find(".images.active").length == 0){
		imgsCont.find(".images").first().addClass("active")
	}
	
	var imgsActive = imgsCont.find(".images.active"),
			activeOffset = imgsActive.offset().top - imgsCont.offset().top
	
	imgs.each( function(){
		var $this = $(this),
				childrenWidth = 0;
		
		$this.children().each(function(){
			childrenWidth += $(this).outerWidth()
		});
		
		$this.width(childrenWidth)
		
	});
	
	imgsCont.css({"transform": "translate(0, -"+ activeOffset +"px)"});
	
	product.find(".options").find("li").eq(imgsActive.index()).addClass("active")
	
	product.find(".options").find("li").on('click', function(e){
		e.preventDefault();
		
		var $this = $(this),
				optIndex = $this.index();
		
		$this.parents("ul").find(".active").removeClass("active");
		$this.addClass("active");
		
		var nextImgs = imgsCont.find(".images").eq(optIndex),
				nextImgsoffset = nextImgs.offset().top - imgsCont.offset().top 
		
		imgsCont.find(".images.active").removeClass("active")
		nextImgs.addClass("active")
	
	imgsCont.css({"transform": "translate(0, -"+ nextImgsoffset +"px)"});
		
	});
	
	imgs.each( function(){
		if ($(this).find(".active").length == 0){
			$(this).find("img").first().addClass("active")
		}
	})
	
	function imgsNextImg(){
		
		var activeImgs = imgsCont.find(".images.active"),
				acImg = activeImgs.find("img.active"),
				imgsImg = activeImgs.find("img"),
				imgLen = imgsImg.length,
				nextImgEq = 0
		
		if (acImg.index() + 1 >  imgLen - 1){
			nextImgEq = 0
		}else{
			nextImgEq = acImg.index() + 1
		}
		
		var nextEq = activeImgs.find("img").eq(nextImgEq),
				nextOffset = nextEq.offset().left - activeImgs.offset().left
		
		
		acImg.removeClass("active");
		nextEq.addClass("active");
		
		activeImgs.css({"transform": "translate(-" + nextOffset + "px, 0)"})
		
	}
	
	function imgsPrevImg(){
		
		var activeImgs = imgsCont.find(".images.active"),
				acImg = activeImgs.find("img.active"),
				imgsImg = activeImgs.find("img"),
				imgLen = imgsImg.length,
				nextImgEq = 0
		
		if (acImg.index() - 1 < 0){
			nextImgEq = imgLen - 1
		}else{
			nextImgEq = acImg.index() - 1
		}
		
		var nextEq = activeImgs.find("img").eq(nextImgEq),
				nextOffset = nextEq.offset().left - activeImgs.offset().left
		
		
		acImg.removeClass("active");
		nextEq.addClass("active");
		
		activeImgs.css({"transform": "translate(-" + nextOffset + "px, 0)"})
		
	}
	
	$(controls).find(".arrows").find(".right").on('click', function(e){
		e.preventDefault();
		imgsNextImg()
	});
	$(controls).find(".arrows").find(".left").on('click', function(e){
		e.preventDefault();
		imgsPrevImg();
	});
	
});