<template>
 <div class="login-container">
   <div class="title">现场计量设备
     <span>运行风险预测与评价软件</span>
   </div>
    <div class="box-wrapper">
      <div class="login-box">
        <div class="login">
          <div class="box-title">
            <h1>登&nbsp;&nbsp;&nbsp;&nbsp;录</h1>
          </div>
          <el-input v-model="userConfig.username" placeholder="输入账号"></el-input>
          <el-input v-model="userConfig.password" placeholder="输入密码" show-password></el-input>
          <el-button type="primary" style="margin-top:10px;" @click="login" class="btnbgcolor">登录</el-button>
           <el-button type="primary" style="margin-top:10px;" @click="toregiste" class="btnbgcolor">去注册</el-button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
/* eslint-disable */ 
import userApi from '@/Api/user-operation'
export default {
  data() {
    return {
     userConfig:{
        username: '',
        password: ''
     },
     passwordAgain: ''
    }
  },
  methods: {
    login() {
      let formData = new FormData()
      formData.append('username', this.userConfig.username)
      formData.append('password', this.userConfig.password)
      userApi.login(formData).then(response => {
        this.$message.success('登录成功')
        window.sessionStorage.setItem("islogined", 1)
        window.sessionStorage.setItem('session',response.data.session)
        window.sessionStorage.setItem('username',this.userConfig.username)
        this.$router.push({
          name: "main",
          query: {
            account: this.userConfig.username
          }
        });
      }).catch(error => {
        this.$message.error('登录失败')
      })
    },
    toregiste () {
      //this.isRegiste = true
      this.$router.push({
        path:'/registe'
      })
    }
  }
};
</script>

<style lang="scss" scope>
@import "../assets/style.scss";
.login-container {
  position: fixed;
  width: 100%;
  height: 100%;
  background: #545c64;
  .title{
    font-family: 'BebasNeueRegular', 'Arial Narrow', Arial, sans-serif;
    font-size: 35px;
    line-height: 35px;
    position: relative;
    font-weight: 400;
    color: rgba(255,255,255,0.9);
    text-shadow: 1px 1px 1px rgba(0,0,0,0.1);
    padding: 80px 0px 5px 0px;
    text-align: center;
    width: 100%;
    span{
      color: #7cbcd6;
      text-shadow: 0px 1px 1px rgba(0,124,119,0.8);
    }
  }
  .box-wrapper {
    width: 100%;
    position: relative;
    height: 300px;
    .login-box {
      width: 500px;
      height: 350px;
      background: #fff;
      // margin: auto;
      position: absolute;
      top: 20%;
      left: 35%;
      border-radius: 10px;
      .login {
        margin: 70px;
        .box-title{
          text-align: center;
          h1{
            color: #007A77;
          }
        }
        .el-input {
          margin-top: 20px;
        }
      }
    }
    .registe-box{
      width: 500px;
      height: 500px;
      background: #fff;
      position: absolute;
      top: 20%;
      left: 35%;
      border-radius: 10px;
      .registe{
        margin: 70px;
        .box-title{
          text-align: center;
          h1{
            color: #007A77;
          }
        }
        .el-input {
          margin-top: 20px;
        }
      }
    }
  }
}
</style>
