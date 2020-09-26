//<script type="text/javascript">
function validate()
{ 
   if( document.registration.name.value == "" )
   {
     alert( "Please provide your Name!" );
     document.registration.name.focus() ;
     return false;
   }
   
   if( document.registration.address.value == "" )
   {
     alert( "Please provide your Address!" );
     document.registration.address.focus() ;
     return false;
   }

 var emailid = document.registration.email.value;
  atpos = emailid.indexOf("@");
  dotpos = emailid.lastIndexOf(".");
 if (emailid == "" || atpos < 1 || ( dotpos - atpos < 2 )) 
 {
     alert("Please enter correct email ID")
     document.registration.email.focus() ;
     return false;
 }

 if( document.registration.link.value == "" )
   {
     alert( "Please provide your Link!" );
     document.registration.link.focus() ;
     return false;
   }

if( document.registration.org_name.value == "" )
   {
     alert( "Need to know your Organisation Name!" );
     document.registration.org_name.focus() ;
     return false;
   }

   if( document.registration.supporter.value == "" )
   {
     alert( "Mention who all are Supporting!" );
     document.registration.supporter.focus() ;
     return false;
   }
   return( true );
}
//</script>
