<template>
  <div class="tagTree">
    <div>
      Current User: {{ this.$route.params.name }}
    </div>

    <div class="block">
      <span class="demonstration">Classification Tree</span>
      <el-cascader
        :options="tree"
        v-model="direc"
        change-on-select="true">
      </el-cascader>
    </div>
    <div>
      Current Class: {{ currentPath.join(': ') }}
    </div>
    <el-button @click=add_class>new class</el-button>
    <el-button @click=add_file>add file</el-button>


    <a v-if=addClass>
      <v-input
        placeholder="input class name"
        v-model="newClass">
      </v-input>
      <v-button
        @click=add_new_class>
        +
      </v-button>
    </a>

    <a v-if=addFile>
    <v-input
      placeholder="input title"
      v-model="newFileTitle">
    </v-input>
    <v-input
      placeholder="input file url"
      v-model="newFileUrl">
    </v-input>
    <v-button
      @click=add_new_file>
      +
    </v-button>
    </a>


    <div>
      <el-dialog>File List:</el-dialog>
      <ul v-for="file in fileList">
        <li>
          <el-button>{{ file }}</el-button>
        </li>
      </ul>
    </div>
  </div>


</template>

<script>
    export default {
      name: 'tagTree',
      data () {
          return {
              fileList: [],
              userId: "10032",
              tree: [],
              direc: [],
              addClass: false,
              addFile: false,
              newClass: "",
              newFileTitle: "",
              newFileUrl: ""
          }
      },
        methods: {

            showTags () {
                this.$http.get('http://127.0.0.1:8080/api/show_classification_tree?username=' + this.$route.params.name)
                    .then((response) => {
                        var res = response;
                        this.tree = res['node'];
                    })
            },
            showFiles () {
                this.$http.get('http://127.0.0.1:8080/api/show_classification_tree?username=' + this.userId)
                    .then((response) => {
                        var res = JSON.parse(response.bodyText)
                        if (res['error_num'] == 0) {
                            this.fileList = res['fileList']
                        } else {
                            console.log('Error: cannot get file list!')
                            this.fileList = []
                        }
                    })
            },
            add_class () {
                this.addClass = true;
            },
            add_new_class () {
                var axios = require('axios')
                var qs = require('qs')
                axios.post('/api/add_classification',
                           qs.stringify({ username: this.userId,
                                          father_name: this.direc.join('.'),
                                          name: this.newClass})
                          )
                    .then((response) => {
                        this.showTags();
                        this.addClass = false;
                    });
            }

            add_file () {
                this.addFile = true;
            },
            add_new_file () {
                var axios = require('axios')
                var qs = require('qs')

            }
        },
        mounted: function() {
      //这个是钩子函数
      //如果cartView函数要执行，必须先执行钩子函数
      //这个钩子函数完成了对cratView函数的调用
      //应该注意的是，使用mounted 并不能保证钩子函数中
      // 的 this.$el 在 document 中。为此还应该引入
      // Vue.nextTick/vm.$nextTick
            this.$nextTick(function () {
                this.userId = this.$route.params.name;
                this.showTags()
                this.showFiles()
            })
        }
    }
</script>
