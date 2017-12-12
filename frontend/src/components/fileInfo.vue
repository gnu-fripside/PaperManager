<template>
    <div class="fileInfo">
    <el-form :model="Paper" :rules="rules" ref="Paper" label-width="100px" class="paperInfo">
      <!-- <el-form-item label="Class" prop="class">
        <el-cascader
          :options="classTree"
          v-model="classes"
          @change="changeClass">
        </el-cascader>
      </el-form-item> -->
      <el-form-item label="Title" prop="title">
        <el-input
          :placeholder="Paper.title"
          v-model="Paper.title">
        </el-input>
      </el-form-item>
      Author:
      <el-row v-for="author in Paper.authors">
        <el-col :span="6">
          <el-form-item
            label="first name"
            :rules="[
                    { required: true, message: 'please input first name', trigger: 'blur' },
                    ]"
            :prop="'first_name_' + author.first_name + '_' + author.last_name" >
            <el-input
              :placeholder="author.first_name"
              v-model="author.first_name">
            </el-input>
          </el-form-item>
        </el-col>
        <el-col :span="6">
          <el-form-item
            label="last name"
            :prop="'last_name_' + author.first_name + '_' + author.last_name"
            :rules="[
                    { required: true, message: 'please input last name', trigger: 'blur' },
                    ]">
            <el-input
              :placeholder="author.last_name"
              v-model="author.last_name">
            </el-input>
          </el-form-item>
        </el-col>
        <el-col :span="6">
          <el-form-item
            label="email"
            :prop="'email_' + author.first_name + '_' + author.last_name"
            :rules="[
                    { required: true, message: 'please input email address', trigger: 'blur' },
                    { type: 'email', message: 'invalid email address', trigger: 'change' }
                    ]">
            <el-input
              :placeholder="author.email"
              v-model="author.email"
              >
            </el-input>
          </el-form-item>
        </el-col>
        <el-button
          @click="deleteAuthor(author)">
          Delete
        </el-button>
      </el-row>
      <el-button
        @click="addAuthor">
        Add Author
      </el-button>
      <el-form-item
        label="Publish Time"
        prop="Publish Time">
        <el-date-picker
          type="date"
          :placeholder="Paper.publish_time"
          v-model="Paper.publish_time">
        </el-date-picker>
      </el-form-item>
      <el-form-item
        label="Source"
        prop="source">
        <el-input
          :placeholder="Paper.source"
          v-model="Paper.source">
        </el-input>
      </el-form-item>
      <el-form-item
        label="URL"
        prop="url">
        <el-input
          :placeholder="Paper.url"
          v-model="Paper.url">
        </el-input>
      </el-form-item>
    </el-form>
    <el-button
      type="primary"
      @click="submitForm">
      Submit Changes
    </el-button>
  </div>
</template>

<script>
    export default {
        name: 'fileInfo',
        data () {
            return {
                Paper: {
                    username: "",
                    title: "",
                    authors: [
                        {
                            first_name: "alah",
                            last_name: "uhak",
                            email: "bah"
                        },
                    ],
                    publish_time: "",
                    add_time: "",
                    source: "",
                    url: "",
                    // classification_tree_node: "",
                    log: ""
                },
                /*
                classTree: [
                ],
                classes: [],
                */
                rules: {
                    title: [
                        { required: true, message: 'title cannot be empty', trigger: 'blur' }
                    ],
                    publish_time: [
                        { type: 'date', required: true, message: 'date cannot be empty', trigger: 'change' }
                    ],
                    source: [
                        { required: true, message: 'source cannot be empty', trigger: 'blur' }
                    ],
                    url: [
                        { required: true, message: 'url cannot be empty', trigger: 'blur' }
                    ]
                    /*
                    ,classes: [
                        { type: 'array', required: true, message: 'class cannot be empty', trigger: 'change' }
                    ]
                    */
                }
            };
        },
        methods: {
            changeClass: function () {
                this.Paper.classification_tree_nodes = this.classes.join('.');
            },
            deleteAuthor: function (author) {
                for (var i = 0; i < this.Paper.authors.length; i++) {
                    if (this.Paper.authors[i].first_name == author.first_name &&
                        this.Paper.authors[i].last_name == author.last_name &&
                        this.Paper.authors[i].email == author.email) {
                        this.Paper.authors.splice(i, 1);
                    }
                }
            },
            addAuthor: function () {
                var newAuthor = {
                    first_name: "",
                    last_name: "",
                    email: ""
                };
                this.Paper.authors.push(newAuthor);
            },
            submitForm: function () {
                var axios = require('axios');
                var qs = require('qs');
                axios.post('/api/update_paper_info',
                           qs.stringify(this.Paper)
                          )
                    .then((response) => {
                        var res = response.data;
                        if (res['error_num'] == 0)
                            alert('Accepted');
                        else
                            alert(res['msg']);
                    });
            },
            getForm: function () {
                var axios = require('axios');
                var qs = require('qs');
                axios.post('/api/show_paper_detail',
                           qs.stringify({username: this.$route.params.name,
                                         hash_code: this.$route.params.hash_code})
                          )
                    .then((response) => {
                        this.Paper = response.data;
                        this.Paper.username = this.$route.params.name;
                    });
            }
        },

        mounted: function() {
            this.$nextTick(function () {
                // this.classes = this.Paper.classification_tree_node.split('.');
                this.getForm();
            });
        }
    }
</script>
