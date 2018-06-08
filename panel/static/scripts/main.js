/*-------Sumbissions Managers-------*/
$('#rooms').on('submit', function(event){
    event.preventDefault();  
    create_room();
});
$('.voting').on('submit', function(event){
	console.log("voting")
    event.preventDefault();
	
   vote();
	
});
$('.Edits').on('submit', function(event){
    event.preventDefault();
  
    EditQ();
});
$('.Delete').on('submit', function(event){
    event.preventDefault();
  
    DeleteQ();
});
$('.DeleteRoom').on('submit', function(event){
    event.preventDefault();
     console.log(DeleteR)
    DeleteR();
});
$('#NewQ').on('submit', function(event){
    event.preventDefault();
    console.log("newQ")
    console.log($('#askroomID').val())
    console.log( $('#CreatedBy').val())
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
	list=[]
    for (i = 0; i < $('.Edits').length; i++) { 
    dict={'confirm':$('.Edits')[i]['confirm']['value'],
          'question_id' : $('.Edits')[i]['qID']['value'],  
          'content':$('.Edits')[i]['content']['value'],       
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
             $('.Edits')[i]['content']['value']= ' '
          	
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


function DeleteR() {
    list=[]
    for (i = 0; i < $('.DeleteRoom').length; i++) { 
    dict={'confirm':$('.DeleteRoom')[i]['confirm']['value'],
          'askroom_id' : $('.DeleteRoom')[i]['rID']['value'],           
          	'IdentifyDeleteRoom' : " "                      
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
	         for (i = 0; i < $('.DeleteRoom').length; i++) { 
             $('.DeleteRoom')[i]['confirm']['value']='No'
           
          	
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
             created_by: $('#CreatedBy').val()
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
    dataToSend= {title : $('#title').val(),
    	     public : $('#public').val(),
    	     description : $('#description').val(),
    	     created_by: $('#CreatedBy').val(),
             IdentifyAddRoom: ' '
        
    }
     jsonText=JSON.stringify(dataToSend)
$.ajax({
    url : "search/", // the endpoint
    type : "POST", // http method
    
    data : {'data1':jsonText
    	  
    
    
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
