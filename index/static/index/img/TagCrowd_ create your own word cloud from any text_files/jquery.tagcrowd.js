/*
 * jQuery functions for TagCrowd.com
 * @copyright Daniel Steinbock, http://tagcrowd.com
 * @version 1.0
 */

// JQUERY FUNCTIONS
$(document).ready(function(){

	// INITIALIZE STUFF
	
	// MODIFY NON-JAVASCRIPT VERSION
	// init save-as button
	$('#save-as').removeClass('save-button-on');

	// init visualize button
	$('#visualize').append('<a href="#">Visualize!</a>');
	$('#tc_submit').addClass("hidden");

	// init source selection
/* 	$('#source-control').removeClass("hidden"); */
/* 	$('#buttons').removeClass("hidden"); */

	// INIT SOURCE CONTROL
	if( $('#tc_form input[@name="source"]:checked').val() == 'url_file' ){
	    $('#source-control').tabs({
	    	fx: { height:'toggle',duration:'fast' },
	    	selected: 1			 // start w/ URL tab selected
	    });
	}
	else if( $('#tc_form input[@name="source"]:checked').val() == 'uploaded_file' ){
	    $('#source-control').tabs({
	    	fx: { height:'toggle',duration:'fast' },
	    	selected: 2			 // start w/ upload tab selected
	    });
	}
	else if( $('#tc_form input[@name="source"]:checked').val() == 'text' ){
	    $('#source-control').tabs({
	    	fx: { height:'toggle',duration:'fast' },
	    	selected: 0			 // start w/ paste tab selected
	    });
	}

	$("#source-control").bind( "tabsselect", function(event, ui) {
		var src = ui.index;
		if( src == 0 ){
			$('#radio-text').attr("checked","checked");
		}
		else if( src == 1 ){
			$('#radio-url').attr("checked","checked");
		}
		else if( src == 2 ){
			$('#radio-upload').attr("checked","checked");
		}
	});


	// FUNCTIONS

	$('a:#embed_link').click(function(event){
		$('#embed_code').toggle('fast');
 		event.preventDefault();
	});

	$('a:#save-as').click(function(event){
		$('#printable').toggle('slide','fast');
		$('#save-as').toggleClass('save-button-on');
		if( $('#embed_code').is(':visible') ){
			$('#embed_code').hide('fast');
		}
 		event.preventDefault();
	});

	$('#stoplist-area').autoResize({
	    // On resize:
	    onResize : function() {
	        $(this).css({opacity:0.8});
	    },
	    // After resize:
	    animateCallback : function() {
	        $(this).css({opacity:1});
	    },
	    // Quite slow animation:
	    animateDuration : 150,
	    // More extra space:
	    extraSpace : 1,
	    limit : 180,
	    animate : true,
	});
	

	$('#tc_form').submit(function() {
		$('#loader').removeClass("hidden");
	});
	
	$('#visualize').click(function(event){
		$('#tc_form').submit();
	  	event.preventDefault();
	});

});
