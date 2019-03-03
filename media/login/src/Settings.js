import cookie from "react-cookie";
import axios from "axios";
import { message } from 'antd';

let baseUrl=""
let csrftoken=cookie.load('csrftoken');
let req=axios.create({baseURL:baseUrl,headers: {'X-CSRFToken': csrftoken}})

req.interceptors.response.use(
    function (response){
        return response;
    },
    function(error){
        let response = error.response;
        if(response){
            if( (response.status!==302)&&(response.data!==undefined)&&(response.data.error_message!==undefined)){
                message.error(response.data.error_message)
            }
            if( (response.status===302)&&(response.data!==undefined)&&(response.data.redirect_url!==undefined)  ){
                window.location.href=response.data.redirect_url;
            }
            if( response.status >=500 ){
                message.error("请检查您的网络连接")
            }
        }
        throw error;
    }
);

export default{
    request:req,
    user_api_url:"/api/v1/user/",
    login_api_url:"/api/v1/login/"
}
