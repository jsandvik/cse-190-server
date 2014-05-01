letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

$(function() {
    // Bind the add/remove answer buttons
    $(".add-answer-btn").click(add_answer);
    $(".remove-answer-btn").click(remove_answer);

    $(".well").each(function() {
        $answers = $(this).find(".answers").children("div")
        if ($answers.length <= 3) {
            $(this).find(".remove-answer-btn").prop('disabled', true);
        }
    });

});

function add_answer() {
    // Get the question box
    var $question_box = $(this).closest(".well");

    var $answers = $question_box.find(".answers");
    var $answer = $answers.children("div").last().clone();

    var num_answers = $answers.children("div").length;
    $answer.find("input").val("");
    $answer.find("span").html(letters[num_answers]);
    $answers.append($answer);

    var $correct_answers = $question_box.find(".correct-answers");
    var $option = $correct_answers.children("option").last().clone();
    $option.html(letters[num_answers]);
    $option.val(parseInt($option.val()) + 1);
    $correct_answers.append($option);

    // Disable the button
    $question_box.find(".remove-answer-btn").prop('disabled', false);
}

function remove_answer() {
    // Get the question box
    var $question_box = $(this).closest(".well");

    var $answers = $question_box.find(".answers").children("div");
    $answers.last().remove();

    var $option = $question_box.find(".correct-answers").children("option");
    $option.last().remove();

    if ($answers.length <= 3) {
        $question_box.find(".remove-answer-btn").prop('disabled', true);
    }
}
