$('#post-form').on('submit', function(event){
    event.preventDefault();
    console.log("form submitted!")  // sanity check
    create_post();
});

// AJAX for posting
function create_question() {
    console.log("create question is working!") // sanity check
    console.log($('#post-text').val())
};