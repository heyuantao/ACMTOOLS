function isEmailValid(email) {
    var re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(String(email).toLowerCase());
}

function formFieldLengthCheck(formData,fieldList){
    let result = ""
    fieldList.entrySeq().forEach( e=>{
        let fieldName = e[0]
        let fieldMaxlength = e[1]
        if( formData.get(fieldName)){
            if(formData.get(fieldName).length>fieldMaxlength){
                result = "字段长度超过限制"
            }
        }
    })
    return result
}
export default{
    isEmailValid:isEmailValid,
    formFieldLengthCheck:formFieldLengthCheck,
}
