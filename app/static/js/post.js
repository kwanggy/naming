
function addNewComment(id) {
    var comments = ""; 
    comments += '<div class="col-md-offset-1 media" style="border-style:groove"> <a class="pull-left" href="#"> <img class="media-object" src=http://www.gettyimages.co.uk/CMS/StaticContent/1365074401896_Justin-Case-1.jpg></a><div class ="media-body"><h5 class=media-heading style="margin-top:10px">User Name</h5><p id="demo"> THIS IS A NEW COMMENT</p></div></div>';
    
    var  newComment="";
    newComment += '<div class="panel2-body"> <div class="media" style="margin-left:7%;border-style:groove"> <a class="pull-left" href="#"> <img class="media-object"  src="http://www.gettyimages.co.uk/CMS/StaticContent/1365074401896_Justin-Case-1.jpg"> </a> <div class="media-body" style="margin-bottom:5px"> <h5 class=media-heading">User Name</h5> <textarea style="width:99%" rows="1" autofocus></textarea> </div> </div> <div class="ids"> <div class="fb"><a href="#"><img src="http://assets.gae9.com/img/btn_share_facebook_small-27882cc2.png" alt="Share to Facebook"></a></div> <div class="tw"><a href="#"><img src="http://assets.gae9.com/img/btn_share_twitter_small-44142e4d.png"></a></div> <div class="gc"><a href="#"><img src="http://lh3.ggpht.com/-XlS02flrqs4/TjBPx4b_E1I/AAAAAAAADWg/HrDTZ8ivUhM/googleplus1_thumb%25255B1%25255D.jpg?imgmax=800"></a></div> </div> <div class="subbutton"><input type="submit" class="btn-danger" value="submit"></div> </div>';
 
    $( id ).append(comments);
    $( id ).append(newComment);
    
}

$(document).ready( function() {
        $("#more1").click(addNewComment('#hidden1'));
        
        $("#more2").click(addNewComment('#hidden2'));
    
    
        $("#more3").click(addNewComment('#hidden3'));
});
