/*-------Sumbissions Managers-------*/
$('#rooms').on('submit', function(event){
    event.preventDefault();  
    create_room();
});
$('.votingplus').on('submit', function(event){
	console.log("votingplus")
    event.preventDefault();
	
   voteplus();
	
});
$('.votingminus').on('submit', function(event){
	console.log("votingminus")
    event.preventDefault();
	
   voteminus();
	
});
$('.Edits').on('submit', function(event){
    event.preventDefault();
    console.log($('.Edits')[0]['content']['value'])
    EditQ();
});
$('.Delete').on('submit', function(event){
    event.preventDefault();
   
    DeleteQ();
});
$('#NewQ').on('submit', function(event){
    event.preventDefault();
    console.log("newQ")
    console.log($('#askroomID').val())
    console.log( $('#CreatedBy').val())
    newQ();
});
/*------Actual Methods---------*/
var currentQuestionId = 0;

function setQuestion(i){
console.log(i);
currentQuestionId = i;
}
function voteplus() {
    list=[]
    for (i = 0; i < $('.votingplus').length; i++) {
		console.log(i)
    dict={'voting':$('.votingplus')[i]['value']['value'],
          'question_id' : $('.votingplus')[i]['question_id']['value'],
		   'user_id': $('.votingplus')[i]['user_id']['value'],
          	'IdentifyVote' : " "
    
	    	     
                 
	    	    
	}
	console.log("id"+currentQuestionId)
    if(dict['voting']!= " "  && dict['question_id']==currentQuestionId)
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
	         for (i = 0; i < $('.votingplus').length; i++) { 
             $('.votingplus')[i]['value']['value']=' '
           
          	
             }
            console.log($('.votingplus'))
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

	function voteminus() {
		list=[]
		for (i = 0; i < $('.votingminus').length; i++) {
			console.log(i)
		dict={'voting':$('.votingminus')[i]['value']['value'],
			  'question_id' : $('.votingminus')[i]['question_id']['value'],
			   'user_id': $('.votingminus')[i]['user_id']['value'],
				  'IdentifyVote' : " "
		
					 
					 
					
		}
		console.log("id"+currentQuestionId)
		if(dict['voting']!= " "  && dict['question_id']==currentQuestionId && list.length == 0)
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
				 for (i = 0; i < $('.votingminus').length; i++) { 
				 $('.votingminus')[i]['value']['value']=' '
			   
				  
				 }
				console.log($('.votingminus'))
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
	list=[]
    for (i = 0; i < $('.Edits').length; i++) { 
    dict={'confirm':$('.Edits')[i]['confirm']['value'],
          'question_id' : $('.Edits')[i]['qID']['value'],  
          'content':    $('.Edits')[0]['content']['value'],       
          	'IdentifyEdit' : " "                      
	    	        }
    if(dict['confirm']== 'Yes')
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
	         for (i = 0; i < $('.Edits').length; i++) { 
             $('.Edits')[i]['confirm']['value']='No'
             $('.Edits')[0]['content']['value']= ' '
          	
             }
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
function DeleteQ() {
    list=[]
    for (i = 0; i < $('.Delete').length; i++) { 
    dict={'confirm':$('.Delete')[i]['confirm']['value'],
          'question_id' : $('.Delete')[i]['qID']['value'],           
          	'IdentifyDelete' : " "                      
	    	        }
    if(dict['confirm']== 'Yes')
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
	         for (i = 0; i < $('.Delete').length; i++) { 
             $('.Delete')[i]['confirm']['value']='No'
           
          	
             }
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
    data1={title : $('#title').val(),
    	     askroomID: $('#askroomID').val(),
    	     content : $('#content').val(),
    	     social_created_by: $('#CreatedBy').val(),
    	     IdentifyQ: $('#IdentifyQ').val(),
             social_created_by: $('#CreatedBy').val()
    }
        
    jsonText=JSON.stringify(data1)
$.ajax({
    url : " ", 
    type : "POST", 
    data : { 'data1':jsonText
    
    
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