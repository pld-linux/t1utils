Summary:	Various utilities for manipulating Type 1 and 2 font programs
Summary(pl.UTF-8):	Różne narzędzia do operowania na fontach Type 1 i 2
Name:		t1utils
Version:	1.33
Release:	1
License:	BSD
Group:		Applications/File
Source0:	http://www.lcdf.org/~eddietwo/type/%{name}-%{version}.tar.gz
# Source0-md5:	a8d9dad4eab239357dd045275770eb8f
URL:		http://www.lcdf.org/~eddietwo/type/#t1utils
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
t1utils is a collection of simple Type 1 and 2 font manipulation
programs. Together, they allow you to convert between PFA (ASCII) and
PFB (binary) formats, disassemble PFA or PFB files into human-readable
form, reassemble them into PFA or PFB format. Additionally you can
extract font resources from a Macintosh font file (ATM/Laserwriter).

%description -l pl.UTF-8
t1utils jest zestawem prostych programów do operowania na fontach
Type 1 i 2. Narzędzia te pozwalają na konwersję pomiędzy formatami PFA
(ASCII) i PFB (binarnym), przekodowanie z PFA lub PFB do postaci
"czytelnej dla człowieka", następnie ponowne złożenie do formatu PFA
lub PFB. Dodatkowo możliwe jest wyciągnięcie fontów z plików fontów z
Macintosha (ATM/Laserwriter).

%prep
%setup -q

%build
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
