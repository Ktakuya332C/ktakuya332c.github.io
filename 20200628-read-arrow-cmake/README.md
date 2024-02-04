# arrowのcmakeファイルを読む

arrowのcmakeファイルを読んで変数の依存関係をまとめてみる。
読む対象は今リリースされている中で一番最新のブランチ
- [maint-0.17.x](https://github.com/apache/arrow/tree/maint-0.17.x)

として、`cpp/CMakeLists.txt`をまとめてみる。

## 概観
このファイルは一つの長いcmakeファイルになっているが、実際にはいくつかのパートに分かれている。
| 対象の行 | 内容 | ラベル |
| --- | --- | --- |
| L21-L57 | バージョン関連設定 | Version |
| L59-L141 | グローバルな変数の設定 | BuildGlobal |
| L145-L184 | ビルドオプションの設定 | BuildOptions |
| L186-L290 | 開発用のターゲット設定 | DevelopTargets |
| L292-L377 | オプション間の依存関係設定 | OptionDependencies |
| L379-L399とL455-L494 | コンパイラフラグの設定 | CompilerFlags |
| L401-L-449 | ビルド成果物のディレクトリ設定 | BuildDirectory |
| L628-L811 | リンカフラグの設定 | LinkerFlags |

以降はそれぞれのパート毎に変数の依存関係を図にしていく。

依存関係の表し方としては
```mermaid
graph LR
  target([target]) --> variable --> subroutine[[subroutine]] & subpart{{subpart}}
```
という形で、ノードの形状でそれぞれの役割を分類することにしている。

## バージョン関連設定(Version)
```mermaid
graph LR
  project[[project]] --> ARROW_BASE_VERSION
  arrow_VERSION_MAJOR --> project[[project]]
  arrow_VERSION_MINOR --> project[[project]]
  arrow_VERSION_PATCH --> project[[project]]
  ARROW_VERSION_MAJOR --> arrow_VERSION_MAJOR
  ARROW_VERSION_MINOR --> arrow_VERSION_MINOR
  ARROW_VERSION_PATCH --> arrow_VERSION_PATCH
  ARROW_SO_VERSION --> ARROW_VERSION_MAJOR & ARROW_VERSION_MINOR
  ARROW_FULL_SO_VERSION --> ARROW_SO_VERSION & ARROW_VERSION_PATCH
  ARROW_BASE_VERSION --> ARROW_VERSION
```

## グローバルな変数の設定(BuildGlobal)
ここでstartはcmakeがデフォルトで生成する変数を生成するプロセス。
```mermaid
graph LR
  CMAKE_BUILD_TYPE --> start[[start]]
  LOWERCASE_BUILD_TYPE --> CMAKE_BUILD_TYPE
  UPPERCASE_BUILD_TYPE --> CMAKE_BUILD_TYPE
  ARROW_SOURCE_DIR --> PROJECT_SOURCE_DIR --> start[[start]]
  ARROW_SOURCE_DIR --> PROJECT_BINARY_DIR --> start[[start]]
  BUILD_SUPPORT_DIR --> CMAKE_SOURCE_DIR --> start[[start]]
  CMAKE_INSTALL_LIBDIR --> GNUInstallDirs[[GNUInstallDirs]]
  PROJECT_NAME --> project[[project]]
  ARROW_CMAKE_INSTALL_DIR --> CMAKE_INSTALL_LIBDIR & PROJECT_NAME
  ARROW_DOC_DIR --> PROJECT_NAME
```

## ビルドオプションの設定(BuildOptions)
ここでanyが依存している変数は任意のターゲットが依存している変数であることを示す。
```mermaid
graph LR
  PYTHON_EXECUTABLE --> CMAKE_VERSION --> start[[start]]
  ARROW_USE_CCACHE --> DefineOptions[[DefineOptions]]
  CCACHE_FOUND --> ARROW_USE_CCACHE
  RULE_LAUNCH_COMPILE --> CCACHE_FOUND
  RULE_LAUNCH_LINK --> CCACHE_FOUND
  any([any]) --> RULE_LAUNCH_COMPILE & RULE_LAUNCH_LINK
  ARROW_OPTION_INSTALL --> DefineOptions[[DefineOptions]]
  CMAKE_SKIP_INSTALL_ALL_DEPENDENCY --> ARROW_OPTION_INSTALL
  INSTALL_IS_OPTIONAL --> ARROW_OPTION_INSTALL
  any([any]) --> CMAKE_SKIP_INSTALL_ALL_DEPENDENCY
```

## 開発用のターゲット設定(DevelopTargets)
DUMMYから始まるノードはいくつかの変数をまとめるために導入したダミー変数。
```mermaid
graph LR
  LINT_EXCLUSIONS_FILE --> BUILD_SUPPORT_DIR --> BuildGlobal{{BuildGlobal}}
  CPPLINT_BIN --> BUILD_SUPPORT_DIR
  PYTHON_EXECUTABLE --> BuildOptions{{BuildOptions}}
  CMAKE_CURRENT_SOURCE_DIR --> start[[start]]
  CLANG_FORMAT_FOUND --> ClangTools[[ClangTools]]
  CLANG_FORMAT_BIN --> ClangTools[[ClangTools]]
  CLANG_TIDY_FOUND --> ClangTools[[ClangTools]]
  CLANG_TIDY_BIN --> ClangTools[[ClangTools]]
  DUMMY1 --> CMAKE_CURRENT_SOURCE_DIR & PYTHON_EXECUTABLE & BUILD_SUPPORT_DIR
  DUMMY2 --> ARROW_LINT_QUIET & LINT_EXCLUSIONS_FILE & DUMMY1
  ARROW_LINT_QUIET --> ARROW_VERBOSE_LINT --> DefineOptions[[DefineOptions]]
  formats([format]) --> CLANG_FORMAT_FOUND & CLANG_FORMAT_BIN & DUMMY2
  check-formats([check-format]) --> CLANG_FORMAT_FOUND & CLANG_FORMAT_BIN & DUMMY2
  clang-tidy([clang-tidy]) --> DUMMY2 & CLANG_TIDY_FOUND & CLANG_TIDY_BIN
  check-clang-tidy([check-clang-tidy]) --> DUMMY2 & CLANG_TIDY_FOUND & CLANG_TIDY_BIN
  lint_cpp_cli([lint_cpp_cli]) --> DUMMY1
  lint([lint]) --> DUMMY2 & CPPLINT_BIN
  UNIX --> start[[start]]
  iwyu([iwyu]) --> BUILD_SUPPORT_DIR & UNIX
  iwyu-all([iwyu-all]) --> BUILD_SUPPORT_DIR & UNIX
```

## オプション間の依存関係設定(OptionDependencies)
```mermaid
graph LR
  ARROW_BUILD_BENCHMARKS --> DefineOptions[[DefineOptions]]
  ARROW_BUILD_INTEGRATION --> DefineOptions[[DefineOptions]]
  ARROW_FUZZING --> DefineOptions[[DefineOptions]]
  ARROW_BUILD_TESTS --> DefineOptions[[DefineOptions]]
  ARROW_JSON --> ARROW_BUILD_BENCHMARKS & ARROW_BUILD_INTEGRATION & ARROW_FUZZING & ARROW_BUILD_TESTS & DefineOptions[[DefineOptions]]
  ARROW_CUDA --> DefineOptions[[DefineOptions]]
  ARROW_FLIGHT --> DefineOptions[[DefineOptions]]
  ARROW_PARQUET --> DefineOptions[[DefineOptions]]
  ARROW_IPC --> ARROW_CUDA & ARROW_FLIGHT & ARROW_PARQUET & ARROW_BUILD_TESTS & DefineOptions[[DefineOptions]]
  ARROW_DATASET --> DefineOptions[[DefineOptions]]
  ARROW_COMPUTE --> ARROW_DATASET & DefineOptions[[DefineOptions]]
  ARROW_FILESYSTEM --> ARROW_DATASET & DefineOptions[[DefineOptions]]
  ARROW_COMPUTE --> ARROW_PQRQUET
  ARROW_PYTHON --> DefineOptions[[DefineOptions]]
  ARROW_COMPUTE --> ARROW_PYTHON
  ARROW_CSV --> ARROW_PYTHON & DefineOptions[[DefineOptions]]
  ARROW_DATASET --> ARROW_PYTHON
  ARROW_FILESYSTEM --> ARROW_PYTHON
  ARROW_HDFS --> ARROW_PYTHON & DefineOptions[[DefineOptions]]
  ARROW_JSOSN --> ARROW_PYTHON
  MSVC --> start[[start]]
  ARROW_ORC --> MSVC & DefineOptions[[DefineOptions]]
  ARROW_USE_GLOG --> MSVC & DefineOptions[[DefineOptions]]
  ARROW_JNI --> DefineOptions[[DefineOptions]]
  ARROW_BUILD_STATIC --> ARROW_JNI & DefineOptions[[DefineOptions]]
  ARROW_WITH_LZ4 --> ARROW_ORC & DefineOptions[[DefineOptions]]
  ARROW_WITH_SNAPPY --> ARROW_ORC & DefineOptions[[DefineOptions]]
  ARROW_WITH_ZLIB --> ARROW_ORC & DefineOptions[[DefineOptions]]
  ARROW_WITH_ZSTD --> ARROW_ORC & DefineOptions[[DefineOptions]]
  NO_TESTS --> ARROW_BUILD_TESTS
  all-tests([all-tests]) --> ARROW_BUILD_TESTS
  unittest([unittest]) --> ARROW_BUILD_TESTS & all-tests([all-tests])
  ARROW_BUILD_EXAMPLES --> DefineOptions[[DefineOptions]]
  NO_EXAMPLES --> ARROW_BUILD_EXAMPLES
  NO_FUZZING --> ARROW_FUZZING
```

## コンパイラフラグの設定(CompilerFlags)
```mermaid
graph LR
  CXX_COMMON_FLAGS --> SetupCxxFlags[[SetupCxxFlags]]
  CMAKE_C_FLAGS --> CXX_COMMON_FLAGS
  CMAKE_CXX_FLAGS --> CXX_COMMON_FLAGS
  ARROW_CXXFLAGS --> DefineOptions[[DefineOptions]]
  CMAKE_CXX_FLAGS --> ARROW_CXXFLAGS
  CXX_ONLY_FLAGS --> SetupCxxFlags[[SetupCxxFlags]]
  CMAKE_CXX_FLAGS --> CXX_ONLY_FLAGS
  ARROW_GENERATE_COVERAGE --> DefineOptions[[DefineOptions]]
  CMAKE_C_FLAGS --> ARROW_GENERATE_COVERAGE
  CMAKE_CXX_FLAGS --> ARROW_GENERATE_COVERAGE
  any([any]) --> CMAKE_C_FLAGS & CMAKE_CXX_FLAGS
```

## ビルド成果物のディレクトリ設定(BuildDirectory)
```mermaid
graph LR
  BUILD_SUBDIR_NAME --> CMAKE_BUILD_TYPE --> start[[start]]
  CMAKE_CURRENT_BINARY_DIR --> start[[start]]
  BUILD_OUTPUT_ROOT_DIRECTORY --> CMAKE_CURRENT_BINARY_DIR & BUILD_SUBDIR_NAME
  CMAKE_ARCHIVE_OUTPUT_DIRECTORY --> BUILD_OUTPUT_ROOT_DIRECTORY
  ARCHIVE_OUTPUT_DIRECTORY --> BUILD_OUTPUT_ROOT_DIRECTORY
  CMAKE_LIBRARY_OUTPUT_DIRECTORY --> BUILD_OUTPUT_ROOT_DIRECTORY
  LIBRARY_OUTPUT_DIRECTORY --> BUILD_OUTPUT_ROOT_DIRECTORY
  EXECUTABLE_OUTPUT_PATH --> BUILD_OUTPUT_ROOT_DIRECTORY
```

## リンカフラグの設定(LinkerFlags)
```mermaid
graph LR
  ARROW_USE_OPENSSL --> DefineOptions[[DefineOptions]]
  ARROW_WITH_BROTLI --> DefineOptions[[DefineOptions]]
  ARROW_WITH_BZ2 --> DefineOptions[[DefineOptions]]
  ARROW_S3 --> DefineOptions[[DefineOptions]]
  ARROW_WITH_LZ4 --> OptionDependencies{{OptionDependencies}}
  ARROW_WITH_SNAPPY --> OptionDependencies{{OptionDependencies}}
  ARROW_WITH_ZLIB --> OptionDependencies{{OptionDependencies}}
  ARROW_WITH_ZSTD --> OptionDependencies{{OptionDependencies}}
  ARROW_ORC --> OptionDependencies{{OptionDependencies}}
  ARROW_USE_GLOG --> OptionDependencies{{OptionDependencies}}
  CMAKE_DL_LIBS --> start[[start]]
  DUMMY1 --> ARROW_USE_OPENSSL & ARROW_WITH_BROTLI & ARROW_ORC & ARROW_USE_GLOG
  DUMMY2 --> DUMMY1 & ARROW_WITH_BROTLI & ARROW_WITH_BZ2 & ARROW_WITH_LZ4 & ARROW_WITH_SNAPPY & ARROW_WITH_ZLIB & ARROW_WITH_ZSTD
  ARROW_LINK_LIBS --> DUMMY1 & ARROW_S3 & CMAKE_DL_LIBS
  ARROW_STATIC_LINK_LIBS --> DUMMY2
  ARROW_STATIC_INSTALL_INTERFACE_LIBS --> DUMMY2 & CMAKE_DL_LIBS
  toolchain([toolchain]) --> ThirdpartyToolchain{{ThirdpartyToolchain}}
  arrow_dependencies([arrow_dependencies]) --> toolchain([toolchain])
  toolchain-tests([toolchain-tests]) --> ThirdpartyToolchain{{ThirdpartyToolchain}}
  arrow_test_dependencie([arrow_test_dependencie]) --> toolchain-tests([toolchain-tests])
  arrow_dependencies([arrow_dependencies]) --> ARROW_STATIC_LINK_LIBS
  ARROW_SHARED_PRIVATE_LINK_LIBS --> ARROW_STATIC_LINK_LIBS
```

途中で複雑すぎて挫折。やはり何かしら別の方法で持って理解するのが良さげ。
