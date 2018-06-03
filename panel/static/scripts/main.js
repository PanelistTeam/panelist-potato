/*-------Sumbissions Managers-------*/
$('#rooms').on('submit', function(event){
    event.preventDefault();  
    create_room();
});
$('#voting').on('submit', function(event){
    event.preventDefault();
    vote();
});
$('#Edits').on('submit', function(event){
    event.preventDefault();
    EditQ();
});
$('#Delete').on('submit', function(event){
    event.preventDefault();
    DeleteQ();
});
$('#NewQ').on('submit', function(event){
    event.preventDefault();
    console.log("newQ")
    console.log($('#askroomID').val())
    newQ();
});
/*------Actual Methods---------*/
function vote() {
	$.ajax({
	    url : " ", // the endpoint
	    type : "POST", // http method
	    
	    data : { question_id : $('#question_id').val(),
	    	     user_id : $('#user_id').val(),	    	     
	    	     IdentifyVote: $('#IdentifyVote').val(),
	    	     value: $('#value').val(),
	    	     csrfmiddlewaretoken: '{% csrf_token %}'
	    
	    
	    }, // data sent with the post request

	    // handle a successful response
	    success : function(json) {
	        $('#data').val(''); // remove the value from the input
	        console.log(json); // log the returned json to the console
	        console.log("success"); // another sanity check
	        location.reload(true);
	        
	    },

	    // handle a non-successful response
	    error : function(xhr,errmsg,err) {
	    	console.log("fail!")
	        $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
	            " <a href='#' class='close'>&times;</a></div>"); // add the error
															// to the dom
	        console.log(xhr.status + ": " + xhr.responseText); // provide a bit
																// more info about
																// the error to the
																// console
	    }
	});
	
	}
//------------------------------------------------------------------------------------------------------//
function EditQ() {
	$.ajax({
	    url : " ", 
	    type : "POST", 
	    dataType: "json",
	    data : { 
	    	     content : $('#content').val(),	    	     
	    	     IdentifyEdit: $('#IdentifyEdit').val(),
	    	     csrfmiddlewaretoken: '{% csrf_token %}',
	    	     qID: $('#qID').val()
	    
	    
	    }, 
	    
	    success : function(json) {
	        $('#data').val(''); 
	        console.log(json); 
	        console.log("success"); 
	        location.reload();
	        
	    },

	    
	    error : function(xhr,errmsg,err) {
	    	console.log("fail!")
	        $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
	            " <a href='#' class='close'>&times;</a></div>"); 
															
	        console.log(xhr.status + ": " + xhr.responseText); 
																
	    }
	});

	}
//------------------------------------------------------------------------------------------------------//
function DeleteQ() {
	$.ajax({
	    url : "search/", // the endpoint
	    type : "POST", // http method
	    data : { title : $('#title').val(),
	    	     public : $('#public').val(),
	    	     description : $('#description').val(),
	    	     social_created_by: $('#CreatedBy').val(),
	    	     csrfmiddlewaretoken: '{% csrf_token %}'
	    
	    
	    }, // data sent with the post request

	    // handle a successful response
	    success : function(json) {
	        $('#data').val(''); // remove the value from the input
	        console.log(json); // log the returned json to the console
	        console.log("success"); // another sanity check
	        location.reload();
	        
	        
	    },

	    // handle a non-successful response
	    error : function(xhr,errmsg,err) {
	    	console.log("fail!")
	        $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
	            " <a href='#' class='close'>&times;</a></div>"); // add the error
															// to the dom
	        console.log(xhr.status + ": " + xhr.responseText); // provide a bit
																// more info about
																// the error to the
																// console
	    }
	});
	return false;
	}
//------------------------------------------------------------------------------------------------------//
function newQ() {
$.ajax({
    url : " ", 
    type : "POST", 
    data : { title : $('#title').val(),
    	     askroomID: $('#askroomID').val(),
    	     content : $('#content').val(),
    	     social_created_by: $('#CreatedBy').val(),
    	     IdentifyQ: $('#IdentifyQ').val(),
    	     csrfmiddlewaretoken: '{% csrf_token %}'
    
    
    }, 
    
    success : function(json) {
        $('#data').val(''); 
        console.log(json); 
        console.log("success"); 
        location.reload(true);
        
    },

    
    error : function(xhr,errmsg,err) {
    	console.log("fail!")
        $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
            " <a href='#' class='close'>&times;</a></div>"); 
														
        console.log(xhr.status + ": " + xhr.responseText); 
															
    }
});

}
//------------------------------------------------------------------------------------------------------//
function create_room() {
$.ajax({
    url : "search/", // the endpoint
    type : "POST", // http method
    data : { title : $('#title').val(),
    	     public : $('#public').val(),
    	     description : $('#description').val(),
    	     social_created_by: $('#CreatedBy').val(),
    	     csrfmiddlewaretoken: '{% csrf_token %}'
    
    
    }, // data sent with the post request

    // handle a successful response
    success : function(json) {
        $('#data').val(''); // remove the value from the input
        console.log(json); // log the returned json to the console
        console.log("success"); // another sanity check
        location.reload();
        
    },

    // handle a non-successful response
    error : function(xhr,errmsg,err) {
    	console.log("fail!")
        $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
            " <a href='#' class='close'>&times;</a></div>"); // add the error
														// to the dom
        console.log(xhr.status + ": " + xhr.responseText); // provide a bit
															// more info about
															// the error to the
															// console
    }
});
return false;
}