<template>
<el-main class="main-bar">
                <div class="main-header">
                   <el-breadcrumb separator="/">
                    <el-breadcrumb-item :to="{ path: '/' }">用户列表</el-breadcrumb-item>
                    </el-breadcrumb>
                </div>
                <div class="main-action">
                   <el-button icon="el-icon-plus" size="small" style="border:none" @click="handleAdd">
                        <span>注册新用户</span>
                   </el-button>
                </div>
                <div class="main-content">
                    <el-table :data="tableData" style="width:100%">
                        <el-table-column type="index" width="75px" label="序号">
                        </el-table-column>
                        <el-table-column label="账号名" prop="username"
                        >
                        </el-table-column>
                        <el-table-column label="操作" width="200px">
                            <template slot-scope="scope">
                                <el-button size="mini" @click="handleDelete(scope.row,scope.$index)" type="danger">删除</el-button>
                            </template>
                        </el-table-column>
                    </el-table>
                        <div class="pagination">
                            <el-pagination
                                :page-size="pagesize"
                                background
                                layout="prev, pager, next"
                                :current-page.sync="pageno"
                                :total="total"
                                @current-change="handlePage"
                                >
                            </el-pagination>
                        </div>
                </div>
            </el-main>
</template>
<script>
/* eslint-disable */
import userApi from '@/Api/user-operation'
export default {
    data(){
        return{
            isCollapse:false,
            titles:[
                {label: "账户名",prop: "username"}
            ],
            tableData:[],
            pagecount: 0,
            total: 0,
            pageno: 1,
            pagesize: 8
        }
    },
    created(){
        this.getUserList()
    },
    methods:{
        getUserList(){
            let formData = new FormData()
            formData.append('pageno', this.pageno)
            formData.append('pagesize', this.pagesize)
            userApi.getUserList(formData).then(response => {
                this.tableData = response.data
            }).catch(error => {
                this.$message.error(error.msg || '获取失败')
            })
        },
        handleCollapse(){
            this.isCollapse = !this.isCollapse
        },
        handleDelete( row , index ){
            const h = this.$createElement
            this.$msgbox({
                title:'删除提示',
                message: h('p',null,[
                    h('span',null,'确定删除用户' + row.username + '?')
                ]),
                showCancelButton:true,
                confirmButtonText:'确定',
                cancelButtonText:'取消',
                callback: action => {
                    if(action === 'confirm'){
                        let form = new FormData()
                        form.append('username',row.username)
                        userApi.userDelete(form).then(response => {
                            this.$message.success('删除成功')
                            this.tableData.splice(index,1)
                        }).catch(error => {
                            this.$message.error('删除失败')
                        })
                    }
                }
            })
        },
        handleAdd(){
            this.$router.push({
                path:'/registe',
            })
        },
         handlePage () {
            this.getFaultList()
        }
    }
}
</script>

<style lang="scss" scope>
@import "../assets/style.scss"
</style>
