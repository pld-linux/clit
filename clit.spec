%define xver %(echo %{version} | tr -d .)
Summary:	Open Convert-.LIT tool
Summary(pl.UTF-8):   Otwarte narzędzie do rozpakowywania plików .LIT
Name:		clit
Version:	1.8
Release:	1
License:	GPL v2+
Group:		Applications/Archiving
Source0:	http://www.kyz.uklinux.net/downloads/open_c-lit-%{version}.tar.gz
# Source0-md5:	d8c599cf0e3cd8bab08e455e51ef852d
URL:		http://www.kyz.uklinux.net/convlit.php
BuildRequires:	libtommath-devel
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
clit allows extracting "DRM1" format .LIT files into their original
XML/HTML. IANAL but using this program may violate DMCA if you're in
USA.

%description -l pl.UTF-8
clit pozwala na rozpakowywanie plików w formacie .LIT/DRM1. Używanie
tego programu na terenie Stanów Zjednoczonych Ameryki Północnej może
być pogwałceniem DMCA.

%prep
%setup -q -c

sed -i -e 's/gcc -o clit.*/$(CC) -o clit $^ -ltommath/' %{name}%{xver}/Makefile

%build
%{__make} -C lib \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -Wall -Ides -Isha -Inewlzx -I."
%{__make} -C %{name}%{xver} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -funsigned-char -Wall -I../lib -I../lib/des -I."

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install %{name}%{xver}/%{name} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
