
$(document).ready(function() {

	$(".initial-expand").hide();
	$(".module-main").hide();

	$("div.module-heading").click(function(){
		$(this).next("div.module-main").slideToggle();

		$(this).children(".expand-collapse-text").toggle();
	});
	
});
