/**
 * Created by Adhaar on 7/27/17.
 */
/**
 * Created by Adhaar on 7/19/17.
 */

//
$(document).ready(function() {
    $("#background_color_input").change(function(){
        var backgroundColor = $("#background_color_input").val();
        $("#sample_quote_div").css("background-color", backgroundColor);

    });

    $("#text_color_input").change(function(){
        var textColor = $("#text_color_input").val();
        $("#sample_quote_div").css("color", textColor);
    });

});


