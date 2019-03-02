import React from "react";
import {fromJS} from "immutable";
import {Icon, Table, Tag} from "antd";
import Settings from "../../Settings";

const req = Settings.request;
const table_data_api_url = Settings.anti_cheating_contest_api_url;

class OneAccountWithMultiIP extends React.Component{
    constructor(props) {
        super(props);
        this.state = {
            contest_id:this.props.contest_id,
            pagination: fromJS({ totalItem: 10, pageSize: 10, pageNumber: 1, needPagination: true }),
            fetching: false,
            tableData: fromJS([]),

        }
    }
    fetchTableListData() {
        const url = table_data_api_url+this.props.contest_id+"/multiip/";
        const params = this.state.pagination.toJS();
        this.setState({fetching:true})
        req.get(url, {params:params}).then(function (response) {
            let tableData = fromJS(response.data.items);
            let paginationData = fromJS(response.data.pagination);
            this.setState({pagination:paginationData});
            this.setState({ tableData: tableData });
            this.setState({fetching:false});
        }.bind(this)).catch(function (error) {
            this.setState({fetching:false});
        }.bind(this))
    }
    componentWillReceiveProps(nextProps, nextContext) {
    }
    componentDidMount() {
        this.fetchTableListData()
    }
    tableColumnFormat() {
        let tableColumn = [
            { title: "用户登录名", dataIndex: "account_id", key: "account_id" },
            { title: "考试编号", dataIndex: "contest_id", key: "contest_id" },
            { title: "用户昵称", dataIndex: "account_nick", key: "account_nick" },
            { title: "使用IP数量", dataIndex: "ip_count", key: "ip_count" },
            {
                title: "状态检查",  key: "summary",
                render: (text, record) => (
                    <div>
                        {(record.ip_count>1)&&<Tag color="red">可疑</Tag>}
                        {(record.ip_count===1)&&<Tag color="blue">正常</Tag>}
                        {(record.ip_count<1)&&<Tag color="magenta">缺考</Tag>}
                    </div>
                )
            },
        ]
        return tableColumn;
    }
    handleTableChange(pagination, filters, sorter){
        let newPagination=fromJS(pagination)
        this.setState({pagination:newPagination},()=>{this.fetchTableListData()})
    }
    handleExpandedRowRender(record){
        return (
            <span>
                {
                    record.ip_list.map( (item,index)=>{
                        return (<Tag color="magenta" key={index} style={{marginBottom:"5px"}}>{item.ip}({item.in_date})</Tag>)
                    })
                }
            </span>
        )
    }
    render() {
        return (
            <div >
                <Table dataSource={this.state.tableData.toJS()} rowKey="id" pagination={this.state.pagination.toJS()}
                       expandedRowRender={this.handleExpandedRowRender}
                       onChange={(pagination, filters, sorter)=>{this.handleTableChange(pagination, filters, sorter)}}
                       columns={this.tableColumnFormat()}
                       loading={this.state.fetching}>
                </Table>
            </div>
        )
    }
}

export default OneAccountWithMultiIP