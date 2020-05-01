/*import React, { Component, Fragment } from "react";
import Header from "./components/Header";
import contact_Us from "./components/contact_Us";
import './index.css';*/


import React, { Component, PropTypes } from 'react';
import 'bootstrap/dist/css/bootstrap.css';
//import 'bootstrap/dist/css/bootstrap-theme.css';
import './App.css';
import axios from "axios";
import cookie from "react-cookies";
import $ from "jquery"

//axios.defaults.xsrfCookieName = "csrftoken";
//axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
//const url ="http://localhost:8000/api/contact_Uss/"
//url.setHeaders({"X-CSRFTOKEN": cookie.load("csrftoken")});

//import React, { Component , PropTypes} from 'react';

import CSRFToken from './csrftoken';

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = $.trim(cookies[i]);
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
  }
var csrftoken = getCookie('csrftoken');

export default class App extends Component{
constructor(){
super();
this.state={ first_name:"",last_name:"",email:"",msg:"" }
}
handleChange = event =>{
this.setState({ [event.target.name]:event.target.value })
}
handleSubmit = event =>{
event.preventDefault();
console.log("first_name : " + this.state.first_name)
console.log("last_name : " + this.state.last_name)
console.log("email :" + this.state.email)
console.log("msg :" + this.state.msg)
const url ="http://localhost:8000/api/contact_Uss/"
const data = { first_name:this.state.first_name,last_name:this.state.last_name ,email:this.state.email,msg:this.state.msg }
fetch(url, { method: "POST", // or ‘PUT’
body: JSON.stringify(data), // data can be `string` or {object}!
headers:{ 'Content-Type': 'application/json','X-CSRFToken': csrftoken} })
.then(res => res.json())
.catch(error => console.error("Error:", error))
.then(response => console.log("Success:", response)); }
render(){
return(
<div>
    <div class="header">
          <div class="container">
            <div class="row">
               <div class="col-xl-3 col-lg-3 col-md-3 col-sm-3 col logo_section">
                   <div class="full">
                     <div class="center-desk">
                         HAGGLE
                     </div>
                   </div>
               </div>
            </div>
          </div>
    </div>
    <div class="brand_color">
           <div class="container">
              <div class="row">
                  <div class="col-md-12">
                      <div class="titlepage">
                        <h2>Contact us</h2>
                      </div>
                  </div>
              </div>
           </div>
    </div>
    <div class="contact">
        <div class="container">
            <div class="row">
                <div class="col-md-12">
                     <form class="main_form " method="post">
                       <CSRFToken/>
                       <div class="row">
                            <div class="col-xl-6 col-lg-6 col-md-6 col-sm-6">
                                    First Name<input class="form-control" type="text" name="First Name" onChange={this.handleChange} /><br></br>
                            </div>
                            <div class="col-xl-6 col-lg-6 col-md-6 col-sm-6">
                                     Last Name<input class="form-control" class="form-control" type="text" name="Last Name" onChange={this.handleChange} /><br></br>
                            </div>
                            <div class="col-xl-6 col-lg-6 col-md-6 col-sm-6">
                                     Email<input class="form-control" type="email" name="email" onChange={this.handleChange} /><br></br>
                            </div>
                            <div class="col-xl-6 col-lg-6 col-md-6 col-sm-6">
                                     Message<input class="form-control" type="text" name="msg" onChange={this.handleChange} /><br></br>
                            </div>
                            <div>
                                    <input class="form-control" type="submit" value="Submit" onclick={this.handleSubmit} />
                            </div>
                        </div>
                     </form> 
                </div>
            </div>
        </div>
    </div>
</div>
)
}
}
//export default App;