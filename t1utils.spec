Summary:     Various utilities for manipulating Type 1 and 2 font programs
Name:        t1utils
Version:     1.10.1
Release:     1
Copyright:   Copyright 1992 Lee Hetherington
Group:       Utilities/File
Source:      http://www.lcdf.org/~eddietwo/type/%{name}-%{version}.tar.gz
URL:         http://www.lcdf.org/~eddietwo/type/
Buildroot:   /tmp/%{name}-%{version}-root

%description
t1utils is a collection of simple Type 1 and 2 font manipulation programs. 
Together, they allow you to convert between PFA (ASCII) and PFB (binary)
formats, disassemble PFA or PFB files into human-readable form, reassemble
them into PFA or PFB format.  Additionally you can extract font resources
from a Macintosh font file (ATM/Laserwriter).

%prep
%setup -q

%build
autoconf
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure %{_target} \
	--prefix=/usr
make

%install
rm -rf $RPM_BUILD_ROOT
#install -d $RPM_BUILD_ROOT/usr/{bin,man/man1}

make install prefix=$RPM_BUILD_ROOT/usr

gzip -9nf $RPM_BUILD_ROOT/usr/share/man/man1/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) /usr/bin/*
/usr/share/man/man1/*

%changelog
* Sun May  9 1999 Tomasz K這czko <kloczek@rudy.mif.pg.gda.pl>
  [1.10.1-1]
- now package is FHS 2.0 compliant.

* Thu Dec  3 1998 Tomasz K這czko <kloczek@rudy.mif.pg.gda.pl>
  [1.7-1]
- added gzipping man pages,
- added using autoconf,
- added -q %setup parameter,
- changed Buildroot to /tmp/%%{name}-%%{version}-root,
- added URL,
- changed base Source url,
- added using %%{name} in Source.

* Mon Jul 13 1998 Peter Soos <sp@osb.hu>
- corrected the permissions of the document directory

* Sun Apr 26 1998 Tomasz K這czko <kloczek@rudy.mif.pg.gda.pl>
  [1.2-2]
- rermoved gziping man pages,
- recompiled against glibc,
- spec file rewrited for using Buildroot,
- added %clean section,
- removed Packager field from spec (if you want recompile package and
  redistribute this package later put this in your private .rpmrc).
- Buildroot changed to /tmp/t1utils-%%{PACKAGE_VERSION}-root,
- added %%{PACKAGE_VERSION} to Source url,
- removed patching Makefile,
- added using $RPM_OPT_FLAGS on compile time,
- added %attr macros in %files (allows building package from
  non-root account).

* Mon Apr 14 1997 Tomasz K這czko <kloczek@rudy.mif.pg.gda.pl>
  [1.2-1]
- spec file rewrited for using Buildroot,
- man pages gziped.
- in CFLAGS changed switch from "-O2" to "-O4 -g",
- added package description.
