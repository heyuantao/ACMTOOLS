import { fromJS } from "immutable";
import * as actionType from "./constants"
let initState=fromJS({path:[""]});

export default function LocationIndicatorReducer(state=initState, action) {
    switch (action.type) {
        case  actionType.LOCATION_CHANGE:
            return state.set("path",action.playload);
        default:
            return state;
    }
}