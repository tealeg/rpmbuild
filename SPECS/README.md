SPECS contains the spec files that define how rpmbuild should build a package.  

If you succesfully build a binary package with rpmbuild, it will result in the spec file being removed.  You can always recover the SPEC file if you have an SRPM so the build stages shuold be:

```sh
# Build the SRPM
rpmbuild -bs <spec-file>
# Buld the binary
rpmbuild --rebuild <SRPM file>
```

And if we want to extract an SRPM into this build tree we simply do the following as a normal user (do not use sudo):

```sh
rpm -i <SRPM File>
```

