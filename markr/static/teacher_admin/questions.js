letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

$(function() {
    // Bind the add/remove answer buttons
    $(".add-answer-btn").click(add_answer);
    $(".remove-answer-btn").click(remove_answer);
});

function add_answer() {
    $(".remove-answer-btn").prop('disabled', false);
    var $answers = $(".answers").children("div");
    var $answer = $answers.last().clone();

    var num_answers = $answers.length;
    $answer.find("span").html(letters[num_answers]);

    $(".answers").append($answer);
}

function remove_answer() {
    var $answers = $(".answers").children("div");
    $answers.last().remove();

    if ($answers.length <= 3) {
        $(".remove-answer-btn").prop('disabled', true);
    }

}