%define xver %(echo %{version} | tr -d .)
Summary:	Open Convert-.LIT tool
Summary(pl):	Otwarte narzêdzie do rozpakowywania plików .LIT
Name:		clit
Version:	1.4
Release:	1
License:	GPL v2+
Group:		Applications/Archiving
Source0:	http://www.kyz.uklinux.net/downloads/open_c-lit-%{version}.tar.gz
# Source0-md5:	f85b2aa1aae9f58102fee9adc29a2cce
URL:		http://www.kyz.uklinux.net/convlit.php
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
clit allows extracting "DRM1" format .LIT files into their original
XML/HTML. IANAL but using this program may violate DMCA if you're in
USA.

%description -l pl
clit pozwala na rozpakowywanie plików w formacie .LIT/DRM1. U¿ywanie
tego programu na terenie Stanów Zjednoczonych Ameryki Pó³nocnej mo¿e
byæ pogwa³ceniem DMCA.

%prep
%setup -q -n %{name}%{xver}src

%build
%{__make} -C lib \
	CC="%{__cc} %{rpmcflags}"
%{__make} -C %{name}%{xver} \
	CC="%{__cc} %{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install %{name}%{xver}/%{name} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{name}%{xver}/{BUGS,CHANGES}
%attr(755,root,root) %{_bindir}/*
