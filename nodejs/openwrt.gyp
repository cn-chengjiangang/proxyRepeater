{
  "make_global_settings": [
      ["CROSS_TOOLCHAIN","/home/zk/wrtnode/staging_dir/toolchain-mipsel_24kec+dsp_gcc-4.8-linaro_uClibc-0.9.33.2/bin"],
      ["CROSS_COMPILE", "$(CROSS_TOOLCHAIN)/mipsel-openwrt-linux-"],
      ["CC", "$(CROSS_COMPILE)gcc"],
      ["CXX", "$(CROSS_COMPILE)g++"],
      ["LINK", "$(CROSS_COMPILE)g++"],
      ["AR", "$(CROSS_COMPILE)ar"]
  ],
  "targets": [{
      "target_name" : "node_nvr_addon",
      "sources" : [ "../src/testSrslibrtmp.cpp" , "../src/cJSON.c", "../src/cMD5.cpp" ],
      "defines" : [
          "NODE_V8_ADDON",
          "SOCKLEN_T=socklen_t",
          "BSD=1"
      ],
      "cflags" :  [
          " -Wno-reorder"
      ],
      "include_dirs" : [
          "../src",
           "../live555/liveMedia/include",
           "../live555/groupsock/include",
           "../live555/BasicUsageEnvironment/include",
           "../live555/UsageEnvironment/include",
           "../srs-librtmp/objs/include"
      ],
      "libraries" : [
           "../../live555/liveMedia/libliveMedia.a",
           "../../live555/groupsock/libgroupsock.a",
           "../../live555/BasicUsageEnvironment/libBasicUsageEnvironment.a",
           "../../live555/UsageEnvironment/libUsageEnvironment.a",
           "../../srs-librtmp/objs/lib/srs_librtmp.a"
      ]
    }]
}