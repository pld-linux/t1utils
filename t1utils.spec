Summary:	Various utilities for manipulating Type 1 and 2 font programs
Summary(pl):	Ró¿ne narzêdzia do operowania na fontach Type 1 i 2
Name:		t1utils
Version:	1.24
Release:	1
License:	Copyright 1992 Lee Hetherington
Group:		Applications/File
Group(de):	Applikationen/Datei
Group(pl):	Aplikacje/Pliki
Source0:	http://www.lcdf.org/~eddietwo/type/%{name}-%{version}.tar.gz
URL:		http://www.lcdf.org/~eddietwo/type/
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
t1utils is a collection of simple Type 1 and 2 font manipulation
programs. Together, they allow you to convert between PFA (ASCII) and
PFB (binary) formats, disassemble PFA or PFB files into human-readable
form, reassemble them into PFA or PFB format. Additionally you can
extract font resources from a Macintosh font file (ATM/Laserwriter).

%description -l pl
t1utils jest kolekcj± prostych programów do manipulacji na fontach
Type 1 i 2. Pozwala na konwersjê pomiêdzy PFA (ASCII) i PFB (binarny),
przekodowaniu z PFA lub PFB do "czytelnej dla cz³owieka" formy, a 
nastêpnie ponowne z³o¿enie do formatu PFA lub PFB. Dodatkowo
mozliwe jest wyci±gniêcie fontów z ATM/Laserwriter z Macintosh'a.

%prep
%setup -q

%build
autoconf
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf NEWS README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
