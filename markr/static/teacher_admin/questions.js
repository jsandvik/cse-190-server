
$(function() {
    // Bind the add/remove answer buttons
    $(".add-answer-btn").click(add_answer);
    $(".remove-answer-btn").click(remove_answer);
});

function add_answer() {
    $(".remove-answer-btn").prop('disabled', false);
}

function remove_answer() {
    $(".remove-answer-btn").prop('disabled', true);

}