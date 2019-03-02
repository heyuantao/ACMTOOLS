import {combineReducers} from "redux";
import UserReducer from "../pages/Common/store/UserReducer";

export default combineReducers(
    {
        user:UserReducer,
    }
)