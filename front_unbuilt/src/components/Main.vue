/*
 * @Author: liuning
 * @Date: 2019-05-28 01:16:37
 * @Last Modified by: mikey.zhaopeng
 * @Last Modified time: 2019-06-18 16:20:41
 */
<template>
    <el-container class="container">
        <el-header class="top-bar">
                <div class="left-bar">
                    <div class="left-bar-brand"><img src="../assets/images/ftlogo.png" alt=""></div>
                    <div class="title">现场计量设备故障自动化诊断与处置知识库</div>
                </div>
                <div class="person-item">
                    <div class="items">
                        <img src="" alt="">
                        <span>{{account}}</span>
                    </div>
                </div>
        </el-header>
        <el-container>
            <el-aside width="200px" class="aside-bar">
                <div class="aside-title">
                    <i class="el-icon-s-flag"></i><span>欢迎系统管理员：{{account}}</span></div>
                <el-row class="">
                    <el-menu default-active="1" class="el-menu-vertical-demo"
                    @open="handleOpen" @close="handleClose"
                    text-color="#000000"
                    active-text-color="#ffd04b"
                    :collapse="isCollapse"
                    >
                        <el-menu-item index="1" @click="handleUserList">
                        <i class="el-icon-user"></i>
                        <span slot="title">用户管理</span>
                        </el-menu-item>
                        <el-submenu index="2">
                        <template slot="title">
                            <i class="el-icon-s-data"></i>
                            <span slot="title" >数据管理</span>
                        </template>
                        <el-menu-item-group>
                            <el-menu-item index="2-1" @click="handleLowPowerUserList">低压用户日用电量</el-menu-item>
                        </el-menu-item-group>
                        </el-submenu>
                        <!-- 知识库录入 -->
                        <el-submenu index="3">
                        <template slot="title">
                            <i class="el-icon-files"></i>
                            <span slot="title" >知识库录入</span>
                        </template>
                        <el-menu-item-group>
                            <el-menu-item index="3-1" @click="handleKnowLedgeHandImport">手动输入知识库</el-menu-item>
                            <el-menu-item index="3-2" @click="handleKnowLedgeExcelImport">批量导入知识库</el-menu-item>
                        </el-menu-item-group>
                        </el-submenu>
                        <!-- 知识库查看 -->
                        <el-submenu index="4" >
                        <template slot="title">
                            <i class="el-icon-thumb"></i>
                            <span slot="title" >查看知识库</span>
                        </template>
                        <el-menu-item-group>
                            <el-menu-item index="4-1" @click="handleKnowLedgeTable">查看知识库数据</el-menu-item>
                        </el-menu-item-group>
                        </el-submenu>
                        <!-- 登出 -->
                        <el-menu-item index="4" @click="handleQuit">
                        <i class="el-icon-s-custom"></i>
                        <span slot="title" >退出</span>
                        </el-menu-item>
                    </el-menu>
                         <!-- <section style="color:#777;font-size:10px;position:absolutel;bottom:80px;">
                            技术支持：武汉大学计算机学院<br>
                            地址：湖北省武汉市武昌区八一路299号武汉大学 <br>
                            邮编：430072 <br>
                            联系电话：027-68775361 <br>
                        </section> -->
                </el-row>
            </el-aside>
            <el-container>
                <router-view></router-view>
            </el-container>
        </el-container>
    </el-container>
</template>
<script>
/* eslint-disable */
import userApi from '@/Api/user-operation'
import nav from '@/nav.config'
export default {
    data(){
        return{
            isCollapse:false,
            account:'admin',
            nav: []
        }
    },
    created(){
        this.account =  window.sessionStorage.getItem('username')
        this.nav = nav
    },
    methods:{
        handleCollapse(){
            this.isCollapse = !this.isCollapse
        },
        handleOpen(){
            
        },
        handleClose(){
            
        },
        handleQuit(){
            let sessionId = window.sessionStorage.getItem('session')
            let formData = new FormData()
            formData.append('session',sessionId)
            userApi.userLoginOut(formData).then(response => {
                this.$message.success('登出成功')
                window.sessionStorage.clear()
                this.$router.push({
                    path:'/login',
                })
            }).catch(error => {
                this.$message.error('登出失败')
            })
        },
        handleLowPowerUserList(){
            this.$router.push({
                name: 'lowPowerUser'
            })
        },
        handleUserList(){
            this.$router.push({
                path:'/main/usertable'
            })
        },
        handleKnowLedgeHandImport(){
            this.$router.push({
                name:'knowledgeImport'
            })
        },
        handleKnowLedgeExcelImport(){
            this.$router.push({
                name:'knowledgeExcelImport'
            })
        },
        handleKnowLedgeTable(){
            this.$router.push({
                name:'knowledgeTable'
            })
        }
    }
}
</script>
<style lang="scss" scope>
.container{
    .top-bar{
        background-image: url('../assets/images/hdbk.jpg');
        display: flex;
        justify-content: space-between;
        color: black;
        min-height: 52px;
        .left-bar{
            .left-bar-brand{
                height: 53px;
                display: inline;
                float: left;
            }
            .title{
                font-size: 18px;
                line-height: 60px; 
                display: inline-block;
                float: right;
                padding-left: 10px;
            }
        }
        .person-item{
            // margin: 15px auto;
            .items{
                margin:15px auto;
                img{
                width: 30px;
                height: 30px;
                }
                span{

                }
            }
        }
    }
    .aside-bar{
        height: 100%;
        .aside-title{
            height: 40px;
            line-height: 40px;
            color:#aeb2b7;
            text-align: center;
            font-size: 13px;
        }
        .el-menu{
            
        }
    }
}
</style>
