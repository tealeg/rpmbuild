SOURCES is used by rpmbuild, but we are expected to provide upstream source packages here in the form of tarballs. 

In the case where we want to pull source code from a version control system, but we don't have direct control over the repository, the easiest solution is often to write a script to grab the source code and build a tarball here that rpmbuild can use.  
