import {fromJS} from "immutable";
import * as actionType from "./constants"
import Settings from "../../../Settings";

const req = Settings.request;
const user_api_url = Settings.user_api_url;

export const getUser = () => {
    return (dispatch)=>{
        let action = {type:actionType.USER_FETCHING,playload:fromJS({})};
        dispatch(action);
        req.get(user_api_url,{}).then((response)=>{
            let action = {type:actionType.USER_FETCHED,playload:fromJS(response.data)};
            dispatch(action)
        }).catch((error)=>{

        })
    }
}

export const logout = () => {
    return (dispatch) => {
        let action = {type:actionType.USER_LOGOUT,playload:fromJS({})};
        dispatch(action);
    }
}
