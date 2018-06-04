/*-------Sumbissions Managers-------*/
$('#rooms').on('submit', function(event){
    event.preventDefault();  
    create_room();
});
$('.voting').on('submit', function(event){
	console.log("voting")
    event.preventDefault();
	//console.log($('.question_id1')[2]['value'])
    console.log($('.voting')[0]['value']['value'])
    
     console.log($('.voting')[2]['IdentifyVote'])
      console.log($('#value').val())
   // console.log($('#question_id'))
   // console.log("qid1")
   // console.log($('#iteration').val())
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
    list=[]
    for (i = 0; i < $('.voting').length; i++) { 
    dict={'voting':$('.voting')[i]['value']['value'],
          'question_id' : $('.voting')[i]['question_id']['value'],
           'user_id': $('.voting')[i]['user_id']['value'],
          	'IdentifyVote' : " "
    
	    	     
                 
	    	    
    }
    if(dict['voting']!= " ")
    {
    list.push(dict)
    }}
    //jsonText=$.serialize(list)
     jsonText=JSON.stringify(list)
    console.log(jsonText)
	$.ajax({
	    url : " ", // the endpoint
	    type : "POST", // http method
	    traditional: true,
	    data : {'data1':jsonText}  	    
	    
	    
	    , // data sent with the post request

	    // handle a successful response
	    success : function(json) {
	         for (i = 0; i < $('.voting').length; i++) { 
             $('.voting')[i]['value']['value']=' '
           
          	
             }
            console.log($('.voting'))
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
function EditQ() {
	$.ajax({
	    url : " ", 
	    type : "POST", 
	    dataType: "json",
	    data : { 
	    	     content : $('#content').val(),	    	     
	    	     IdentifyEdit: $('#IdentifyEdit').val(),
	    	   
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
    	  
    
    
    }, // data sent with the post request

    // handle a successful response
    success : function(json) {
        $('#title').prop('');
        $('#description').prop('');        // remove the value from the input
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