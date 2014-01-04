room = {
  room_id: -1,
  last_update_at: 0,
  update: function( data ){
    data = $.evalJSON( data );
    if ( data.error !== undefined ) {
      $( ".chat-receive" ).text( data.error );
      clearInterval( this.interval );
      return;
    } else if ( room.last_update_at < data.time ) {
      room_last_update_at = data.time;
      var pos = $( ".chat-receive" ).scrollTop();
      var listHeight = $( ".chat-receive .msg-list" ).height();
      $( ".chat-receive .msg-list" ).empty();
      $.each( data.response, function( i, v ) {
        var elem = $( "<div></div>" );
        elem.addClass( ".msg" );
        elem.text( v );
        $( ".chat-receive .msg-list" ).append( elem );
      });
      console.log([ pos, listHeight, $( ".chat-receive" ).height() ]);
      if ( pos >= listHeight - $( ".chat-receive" ).height() ) {
        pos = $( ".chat-receive .msg-list" ).height();
      }
      $( ".chat-receive" ).scrollTop( pos );
    }
  },
  read: function() {
    var url = '/' + this.room_id + '/read';
    $.ajax({
      type: 'GET',
      url: url,
      success: $.proxy( this.update, this )
    });
  },
  write: function( author, message ) {
    var url = '/' + this.room_id + '/write';
    $.ajax({
      type: 'POST',
      url: url,
      data: {
        author: author,
        message: message
      },
      success: $.proxy( this.update, this )
    });
  }
};
room.interval = setInterval( $.proxy( room.read, room ), 1000);
