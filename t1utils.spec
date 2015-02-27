Summary:	Various utilities for manipulating Type 1 and 2 font programs
Summary(pl.UTF-8):	Różne narzędzia do operowania na fontach Type 1 i 2
Name:		t1utils
Version:	1.38
Release:	2
License:	BSD
Group:		Applications/File
Source0:	http://www.lcdf.org/~eddietwo/type/%{name}-%{version}.tar.gz
# Source0-md5:	0c823a7fff74d206ecccb98bfcb1053b
URL:		http://www.lcdf.org/~eddietwo/type/#t1utils
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
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
%{__aclocal}
%{__automake}
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
%attr(755,root,root) %{_bindir}/t1ascii
%attr(755,root,root) %{_bindir}/t1asm
%attr(755,root,root) %{_bindir}/t1binary
%attr(755,root,root) %{_bindir}/t1disasm
%attr(755,root,root) %{_bindir}/t1mac
%attr(755,root,root) %{_bindir}/t1unmac
%{_mandir}/man1/t1ascii.1*
%{_mandir}/man1/t1asm.1*
%{_mandir}/man1/t1binary.1*
%{_mandir}/man1/t1disasm.1*
%{_mandir}/man1/t1mac.1*
%{_mandir}/man1/t1unmac.1*
