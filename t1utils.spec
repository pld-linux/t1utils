Summary:	Various utilities for manipulating Type 1 and 2 font programs
Name:		t1utils
Version:	1.19
Release:	1
License:	Copyright 1992 Lee Hetherington
Group:		Utilities/File
Group(pl):	Narzêdzia/Pliki
Source0:	http://www.lcdf.org/~eddietwo/type/%{name}-%{version}.tar.gz
URL:		http://www.lcdf.org/~eddietwo/type/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
t1utils is a collection of simple Type 1 and 2 font manipulation
programs. Together, they allow you to convert between PFA (ASCII) and
PFB (binary) formats, disassemble PFA or PFB files into human-readable
form, reassemble them into PFA or PFB format. Additionally you can
extract font resources from a Macintosh font file (ATM/Laserwriter).

%prep
%setup -q

%build
LDFLAGS="-s"; export LDFLAGS
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/* \
	NEWS README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
