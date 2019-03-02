import {combineReducers} from "redux";
import UserReducer from "../pages/Common/store/UserReducer";
import LocationIndicatorReducer from "../pages/Common/store/LocationIndicatorReducer";

export default combineReducers(
    {
        user:UserReducer,
        location:LocationIndicatorReducer,
    }
)