<template>
  <div v-if="visible" class="modal">
    <div class="modal-mask"></div>
    <div class="modal-container">
        <div class="el-icon-close close-detail" @click="close"></div>
      <div class="modal-body">
        <span class="title">标题：{{this.fileDetail.title }}</span>
        <span class="author">作者：{{ this.fileDetail.author }}</span>
        <span class="field">文献领域：{{ this.fileDetail.field }}</span>
        <span class="create_time"
          >上传时间：{{ this.fileDetail.create_time }}</span
        >
        <span class="update_time"
          >最后更新时间：{{ this.fileDetail.update_time }}</span
        >
        <span class="auditor">审核员：{{ this.fileDetail.auditor }}</span>
        <el-input
          type="textarea"
          :autosize="{ minRows: 14, maxRows: 20 }"
          v-model="this.fileDetail.content"
          :readonly="this.Permission.Onlyread"
          class="content"
        >
        </el-input>
      </div>
      <div class="modal-footer" v-show="this.$store.getters.getIdentity">
        <button
          @click="fail"
          class="modal-btn"
          v-show="this.Permission.examine"
          
        >
          退回
        </button>
        <button
          @click="success"
          class="modal-btn"
          v-show="this.Permission.examine"
        >
          通过
        </button>
        <button
          @click="change"
          class="modal-btn"
          v-show="!this.Permission.Onlyread"
        >
          修改
        </button>
      </div>
    </div>
  </div>
</template>
  
  <script>
export default {
  name: "CustomModal",
  props: {
    visible: Boolean,
    data: Object,
    Permission: Object,
  },
  data() {
    return {
      fileDetail: Object.assign({}, this.data),
    };
  },
  methods: {
    close() {
      this.$emit("close");
    },
    change() {},
    fail(){},
    success(){},
  },
  watch: {
    data: {
      handler(newVal) {
        this.fileDetail = Object.assign({}, newVal);
      },
      deep: true,
    },
  },
};
</script>
  
  <style scoped>
.modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}

.modal-mask {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
}

.modal-container {
  width: 80%;
  height: 70%;
  max-width: 800px;
  background-color: #fff;
  border-radius: 5px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.3);
  padding: 20px;
  z-index: 999;
}

.modal-title {
  margin: 0;
}

.modal-close-btn {
  border: none;
  background-color: transparent;
  font-size: 20px;
  cursor: pointer;
  outline: none;
}

.modal-body {
  margin-top: 20px;
  margin-bottom: 20px;
  position: relative;
}

.modal-footer {
  /* display: flex;
  justify-content: flex-end; */
  position: relative;
  margin-top: 430px;
  margin-left: 50px;
}

.modal-footer button {
  border-radius: 10px;
  background-color: #5e85bf;
  float: right;
  right: 100px;
}
.modal-btn {
  margin-left: 10px;
  padding: 5px 10px;
  border-radius: 3px;
  border: none;
  color: #fff;
  background-color: #007bff;
  cursor: pointer;
  outline: none;
}

.modal-btn:hover {
  background-color: #0069d9;
}

.close-detail {
    position: absolute;
    right: 350px;
    top: 125px;
    font-size: 20px;
    cursor: pointer;
}
.title {
    position: absolute;
    top: -10px;
    left: 20px;
}
.author {
    position: absolute;
    top: 20px;
    left: 20px;
}
.field {
    position: absolute;
    top: 50px;
    left: 20px;
}
.content {
    position: absolute;
    top: 90px;
    width: 700px;
    left: 20px;
}
.create_time {
    position: absolute;
    top: 410px;
    left: 20px;
    font-size: 12px;
}
.update_time {
    position: absolute;
    top: 425px;
    left: 20px;
    font-size: 12px;
}

.auditor {
    position: absolute;
    top: 440px;
    left: 20px;
    font-size: 12px;
}
</style>
  